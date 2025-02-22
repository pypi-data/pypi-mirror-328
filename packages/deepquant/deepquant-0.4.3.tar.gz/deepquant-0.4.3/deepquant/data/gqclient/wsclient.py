#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import queue
import random
import ssl
import threading
import time
from queue import Queue

import websocket
from websocket import ABNF
from distutils.version import LooseVersion

from google.protobuf import any_pb2, json_format
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import wrappers_pb2
from google.protobuf.message import Message as PB_Message

from . import hclient
from .commons import ApiResponse, ApiRspCode
from .wshandler import BaseDataHandler, BaseMDPushSpi, LogHandler, SubDataType, VarietyCategoryType, MarketType
from .wshandler import ReplayCondition
from ..proto import sdk_message_pb2
from ..proto import real_time_md_pb2
from ..proto import market_data_pb2
from ..proto import proto_utils
from ..proto import replay_pb2
from ..proto import realtime_factor_data_pb2
from ..proto import realtime_factor_server_pb2
from ..utils.gqconfig import configs
from ..utils.log_writer import log

_sym_db = _symbol_database.Default()

_ws_log_type_url = "type.googleapis.com/" + sdk_message_pb2._WSLOGMSG.full_name

_support_header_method = False

if LooseVersion(websocket.__version__) >= LooseVersion('1.6.2'):
    # websocket-client 1.6.2 version support header callable
    _support_header_method = True


class WsClient:
    def __init__(self):
        self.user_id = None
        self.req_client = None

        self.url = None
        self.verify_ssl = True
        self.conn_id = None
        self.header_params = {}

        self._log_handler = LogHandler()
        self._md_push_handlers = []
        self._replay_handlers = []
        self._factor_handlers = []

        self._push_data_q = Queue()
        self._push_data_t = None

        self.ws = None
        self.ws_run_t = None

        self.is_init = False
        self.is_connected = False

    def init(self, req_client) -> [bool, str]:
        if not req_client.is_init:
            log.info('初始化失败-请先进行Client登录')
            return False, "请先进行Client登录"
        self.req_client = req_client
        self.user_id = req_client.user_id

        self.url = configs.get_server_ws() + '/gid/data/websocket'
        self.verify_ssl = configs.is_verify_ssl()
        self.conn_id = f'{int(time.time() * 1000000)}.{random.randrange(0, 1000)}'
        _header_params = self._get_ws_headers(False)
        if isinstance(_header_params, ApiResponse) and not _header_params.is_success():
            log.info('初始化失败-%s', _header_params.msg)
            return False, _header_params.msg
        self.is_init = True
        log.info('初始化完成')
        return True, '初始化完成'

    def start(self) -> [bool, str]:
        if not self.is_init:
            log.warn('未进行初始化，请先调用init')
            return False, '未进行初始化，请先调用init'
        _header_params = self._get_ws_headers(False)
        if isinstance(_header_params, ApiResponse) and not _header_params.is_success():
            log.info('初始化失败-%s', _header_params.msg)
            return False, _header_params.msg
        log.info('WsClientThread starting...')
        # 清空队列
        while not self._push_data_q.empty():
            self._push_data_q.get()
        self._push_data_t = WsClient.PushDataQueueThread(self._push_data_q)
        # 增加日志处理函数
        self._push_data_t.set_log_handler(self._log_handler)
        # 增加行情处理函数
        self._push_data_t.set_md_handler(self._md_push_handlers)
        self._push_data_t.set_replay_handler(self._replay_handlers)
        self._push_data_t.set_factor_handler(self._factor_handlers)
        self._push_data_t.start()

        if _support_header_method:
            # 如不支持，则直接使用之前获得header参数
            _header_params = self._get_ws_headers
        # 创建ws对象不会自动进行连接
        self.ws = websocket.WebSocketApp(self.url,
                                         header=_header_params,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_open=self.on_open,
                                         on_close=self.on_close,
                                         )
        self.ws.keep_running = True
        sslopt = None
        if not self.verify_ssl:
            # 设置不检查SSL证书
            sslopt = {
                "cert_reqs": ssl.CERT_NONE
            }

        self.ws_run_t = threading.Thread(target=lambda: self.ws.run_forever(ping_interval=3,
                                                                            ping_payload='ping',
                                                                            reconnect=3,
                                                                            sslopt=sslopt,
                                                                            )
                                         )
        self.ws_run_t.daemon = True
        self.ws_run_t.start()
        log.info('WsClientThread started')
        log.info('已启动')
        return True, '已启动'

    def _get_ws_headers(self, ignore_failed=True):
        self.header_params['sdkConnId'] = self.conn_id
        token_res = self.req_client.get_token()
        if not token_res.is_success():
            if ignore_failed:
                log.warn('_get_ws_headers-获取token失败-%s', token_res.msg)
                return self.header_params
            else:
                log.error('_get_ws_headers-获取token失败-%s', token_res.msg)
                return token_res
        else:
            self.header_params['Authorization'] = token_res.data
            return self.header_params

    def stop(self) -> [bool, str]:
        if not self.is_init:
            log.warn('未进行初始化，请先调用init')
            return False, '未进行初始化，请先调用init'
        log.info('WsClientThread stopping')
        # 清空队列
        while not self._push_data_q.empty():
            self._push_data_q.get()
        if self._push_data_t is not None:
            self._push_data_t.stop()
            log.info('_push_data_t stopped')

        self.ws.keep_running = False
        if self.ws_run_t is not None:
            self.ws_run_t.join()
            log.info('ws_run_t stopped')
        self.ws.close()

        log.info('WsClientThread stopped')
        return True, None

    def subscribe_md(self,
                     quote_type: SubDataType,
                     security_codes=None,
                     market: MarketType = None,
                     category_type: VarietyCategoryType = None) -> [bool, str]:
        """
        :param quote_type: 行情订阅的数据类型，必传
        :param security_codes: 行情订阅的股票代码，数组[]，传入多个股票代码，如['000001.SZ', '600000.SH']
        :param market: 行情订阅的市场，如需按照市场订阅，则可security_codes不传，market传入需要订阅的市场
        :param category_type: 订阅数据的品种类型，按照市场订阅时，需要指定订阅的标的品种类型，按照股票代码订阅不传
        """
        log.info('subscribe_md_req-start, quote_type=%s, security_codes=%s', quote_type, security_codes)
        pb_sub_req = real_time_md_pb2.SubscribeReq()
        pb_sub_req.type = real_time_md_pb2.ADD
        if security_codes is None or len(security_codes) <= 0 and market is not None and category_type is not None:
            pb_sub_item = real_time_md_pb2.SubscribeItem(
                market=market.value,
                category_type=category_type.value)
            pb_sub_req.sub_items.append(pb_sub_item)
        else:
            for security_code in security_codes:
                pb_sub_item = real_time_md_pb2.SubscribeItem(
                    quote_type=quote_type.value,
                    security_code=security_code)
                pb_sub_req.sub_items.append(pb_sub_item)
        return self.send_message(sdk_message_pb2.M_MARKETDATA, pb_sub_req)

    def unsubscribe_md(self,
                       quote_type: SubDataType,
                       security_codes=None,
                       market: MarketType = None,
                       category_type: VarietyCategoryType = None) -> [bool, str]:
        """
        :params : sub_items为多个sub_item
        """
        log.info('subscribe_md_req-start, quote_type=%s, security_codes=%s', quote_type, security_codes)
        pb_sub_req = real_time_md_pb2.SubscribeReq()
        pb_sub_req.type = real_time_md_pb2.DEL
        if security_codes is None or len(security_codes) <= 0 and market is not None and category_type is not None:
            pb_sub_item = real_time_md_pb2.SubscribeItem(
                market=market.value,
                category_type=category_type.value)
            pb_sub_req.sub_items.append(pb_sub_item)
        else:
            for security_code in security_codes:
                pb_sub_item = real_time_md_pb2.SubscribeItem(
                    quote_type=quote_type.value,
                    security_code=security_code)
                pb_sub_req.sub_items.append(pb_sub_item)
        return self.send_message(sdk_message_pb2.M_MARKETDATA, pb_sub_req)

    def replay_req(self,
                   replay_conditions=None,
                   security_codes=None,
                   market: MarketType = None,
                   category_type: VarietyCategoryType = None,
                   start_time: str = None,
                   end_time: str = None,
                   ) -> [bool, str]:
        """
        :param replay_conditions: 查询数据类别及字段，类型参照 ReplayCondition，必传
        :param security_codes: 数据回放的股票代码，股票代码，数组[]，传入多个股票代码，如['000001.SZ', '600000.SH']
        :param market: 数据回放的市场，TODO 暂不支持按照市场进行回放
        :param category_type: 回放数据的品种类型，按照市场订阅时，需要指定订阅的标的品种类型，按照股票代码订阅不传
        :param start_time: 数据回放的开始时间，格式为 %Y-%m-%d %H:%M:%S.%f， 如'2024-01-02 00:00:00.000'
        :param end_time: 数据回放的截止时间，格式为 %Y-%m-%d %H:%M:%S.%f， 如'2024-01-31 23:59:59.999'
        """
        if replay_conditions is None:
            replay_conditions = []
        log.info('replay_req-start, quote_conditions=%s, security_codes=%s, market=%s, category_type=%s, '
                 'start_time=%s, end_time=%s',
                 replay_conditions, security_codes, market, category_type, start_time, end_time)
        conditions = []
        if len(replay_conditions) > 0:
            for replay_condition in replay_conditions:
                conditions.append(
                    replay_pb2.Condition(
                        quote_type=replay_condition.data_type.value,
                        fields=replay_condition.replay_fields
                    )
                )
        replay_req = replay_pb2.ReplayReq(
            condition=conditions,
            symbols=security_codes,
            start_time=start_time,
            end_time=end_time
        )
        if market is not None:
            replay_req.market = market.value
        if category_type is not None:
            replay_req.variety = category_type.value

        return self.send_message(sdk_message_pb2.M_REPLAYDATA, replay_req)

    def subscribe_factor(self,
                         factor_name: str = None,
                         security_codes=None,
                         market: MarketType = None) -> [bool, str]:
        """
        :param factor_name: 因子订阅名称
        :param security_codes: 因子订阅的股票代码，数组[]，传入多个股票代码，如['000001.SZ', '600000.SH']
        :param market: 因子订阅的市场，如需按照市场订阅，则可security_codes不传，market传入需要订阅的市场
        """
        log.info('subscribe_factor-start, factor_name=%s, market=%s, security_codes=%s',
                 factor_name, market, security_codes)
        pb_sub_req = realtime_factor_server_pb2.SubscribeFactorReq()
        pb_sub_req.type = real_time_md_pb2.ADD
        if security_codes is None or len(security_codes) <= 0 and market is not None:
            pb_sub_item = realtime_factor_server_pb2.SubscribeFactor(
                factor_name=factor_name,
                market=market.value)
            pb_sub_req.sub_factors.append(pb_sub_item)
        else:
            for security_code in security_codes:
                pb_sub_item = realtime_factor_server_pb2.SubscribeFactor(
                    factor_name=factor_name,
                    security_code=security_code)
                pb_sub_req.sub_factors.append(pb_sub_item)
        return self.send_message(sdk_message_pb2.M_FACTOR, pb_sub_req)

    def unsubscribe_factor(self,
                           factor_name: str = None,
                           security_codes=None,
                           market: MarketType = None) -> [bool, str]:
        """
        :param factor_name: 因子订阅名称
        :param security_codes: 因子订阅的股票代码，数组[]，传入多个股票代码，如['000001.SZ', '600000.SH']
        :param market: 因子订阅的市场，如需按照市场订阅，则可security_codes不传，market传入需要订阅的市场
        """
        log.info('unsubscribe_factor-start, factor_name=%s, market=%s, security_codes=%s',
                 factor_name, market, security_codes)
        pb_sub_req = realtime_factor_server_pb2.SubscribeFactorReq()
        pb_sub_req.type = real_time_md_pb2.DEL
        if security_codes is None or len(security_codes) <= 0 and market is not None:
            pb_sub_item = realtime_factor_server_pb2.SubscribeFactor(
                factor_name=factor_name,
                market=market.value)
            pb_sub_req.sub_factors.append(pb_sub_item)
        else:
            for security_code in security_codes:
                pb_sub_item = realtime_factor_server_pb2.SubscribeFactor(
                    factor_name=factor_name,
                    security_code=security_code)
                pb_sub_req.sub_factors.append(pb_sub_item)
        return self.send_message(sdk_message_pb2.M_FACTOR, pb_sub_req)

    def send_message(self, mod_type, data) -> [bool, str]:
        """
        发送消息
        :param mod_type:    业务模块，参照sdk_message_pb2.M_枚举，如 M_MARKETDATA..等
        :param data:  消息参数，发送消息的参数，如{
        :return:
        """
        if not self.is_connected:
            log.error('发送失败-未连接!! mod_type=%s, data=%s', mod_type, data)
            return False, '发送失败-未连接'
        log.info('send_message-start, mod_type=%s, data=%s', mod_type, data)
        # 发送连接信息
        # sub_req = sdk_message_pb2.WsSubReq(sdk_conn_id=self.conn_id, trace_id=hclient.get_uid(), mod_type=mod_type)
        sub_req = sdk_message_pb2.WsSubReq(sdk_conn_id=self.conn_id,
                                           trace_id=hclient.get_uid(),
                                           mod_type=mod_type)
        if isinstance(data, str):
            # 对传入基本类型字符串进行封装
            data = wrappers_pb2.StringValue(value=data)

        if isinstance(data, PB_Message):
            sub_req.param.type_url = "type.googleapis.com/" + data.DESCRIPTOR.full_name
            sub_req.param.value = data.SerializeToString()
            # 此处不直接调用send_bytes 部分低版本的websocket-client没有封装send_bytes接口
            self.ws.send(sub_req.SerializeToString(), ABNF.OPCODE_BINARY)
        else:
            # 此处不直接调用send_bytes 部分低版本的websocket-client没有封装send_bytes接口
            self.ws.send(sub_req.SerializeToString(), ABNF.OPCODE_BINARY)
        log.info('send_message-finish, sub_req=%s', proto_utils.log_pb_obj(sub_req))
        return True, None

    def on_message(self, ws, message):
        # 定义on_message事件回调函数
        _timestamp = int(time.time() * 1000)
        if isinstance(message, str):
            if 'ERR' in message:
                log.error('on_message - %s', message)
            else:
                log.info('on_message - %s', message)
            self._push_data_q.put(message)
        elif isinstance(message, bytes):
            try:
                push_data = sdk_message_pb2.WsPushData()
                push_data.ParseFromString(message)
                push_data.timestamps.append(_timestamp)
                self._push_data_q.put(push_data)
            except Exception as e:
                # 如果抛出异常，则认为解析异常
                log.error('[推送数据异常]- on bytes ParserError: %s', message, e)
                return
        else:
            log.error('[推送数据异常]-未处理的数据类型: %s', message)

    def on_open(self, ws):
        log.info("### on opened ###")
        self.is_connected = True
        # 发送连接信息
        _user_report = sdk_message_pb2.UserConnectedReport(user_id=self.user_id)
        self.send_message(sdk_message_pb2.M_BASE, _user_report)

    # 定义on_error事件回调函数
    def on_error(self, ws, error):
        log.error("### on error ### error= %s", error)
        self.is_connected = False

    # 定义on_open事件回调函数
    def on_close(self, ws, error, msg):
        self.is_connected = False
        log.error("### on closed ### error= %s msg=%s", error, msg)
        self.ws.close()

    def add_md_handler(self, md_push_handler: BaseMDPushSpi):
        log.info("### on add_md_handler ### md_push_handler=%s", md_push_handler)
        self._md_push_handlers.append(md_push_handler)
        if self._push_data_t is not None:
            self._push_data_t.set_md_handler(self._md_push_handlers)

    def clear_md_handler(self):
        log.info("### clear_md_handler")
        if self._md_push_handlers is not None:
            self._md_push_handlers.clear()
        if self._push_data_t is not None:
            self._push_data_t.set_md_handler(self._md_push_handlers)

    def add_replay_handler(self, replay_handler: BaseMDPushSpi):
        log.info("### on add_replay_handler ### replay_handler=%s", replay_handler)
        self._replay_handlers.append(replay_handler)
        if self._push_data_t is not None:
            self._push_data_t.set_md_handler(self._replay_handlers)

    def clear_replay_handler(self):
        log.info("### clear_replay_handler")
        if self._replay_handlers is not None:
            self._replay_handlers.clear()
        if self._push_data_t is not None:
            self._push_data_t.set_md_handler(self._replay_handlers)

    def add_factor_handler(self, md_push_handler: BaseMDPushSpi):
        log.info("### on add_factor_handler ### md_push_handler=%s", md_push_handler)
        self._factor_handlers.append(md_push_handler)
        if self._push_data_t is not None:
            self._push_data_t.set_factor_handler(self._factor_handlers)

    def clear_factor_handler(self):
        log.info("### clear_factor_handler")
        if self._factor_handlers is not None:
            self._factor_handlers.clear()
        if self._push_data_t is not None:
            self._push_data_t.set_factor_handler(self._factor_handlers)

    def set_log_handler(self, log_handler: LogHandler):
        self._log_handler = log_handler

    class PushDataQueueThread(threading.Thread):
        def __init__(self, _q_push_data):
            threading.Thread.__init__(self)
            self.q_push_data = _q_push_data
            self._log_handler = None
            # 业务模块数据回调处理，key=mod_type，value=PushDataHandler
            self._base_handlers = [BaseDataHandler()]
            self._md_push_handlers = []
            self._factor_handlers = []
            self._replay_handlers = []
            self.is_running = False

        def run(self):
            self.is_running = True
            self._deal_push_data()

        def stop(self):
            log.info('PushDataQueueThread stopping')
            self.is_running = False

        def set_log_handler(self, _log_handler):
            self._log_handler = _log_handler

        def set_md_handler(self, md_push_handlers):
            self._md_push_handlers = md_push_handlers

        def set_replay_handler(self, replay_handlers):
            self._replay_handlers = replay_handlers

        def set_factor_handler(self, factor_handlers):
            self._factor_handlers = factor_handlers

        def _deal_push_data(self):
            while self.is_running:
                try:
                    ws_push_data = self.q_push_data.get(block=True, timeout=10)
                    _t_queue_get = int(time.time() * 1000)
                    ws_push_data.timestamps.append(_t_queue_get)
                    if isinstance(ws_push_data, sdk_message_pb2.WsPushData):
                        if ws_push_data.data.type_url == _ws_log_type_url:
                            if self._log_handler is not None:
                                data_type, data_evt, error = proto_utils.parse_any_obj(ws_push_data.data)
                                self._log_handler.on_push_log(
                                    log_level=data_evt.get('level'),
                                    log_timestamp=data_evt.get('log_timestamp'),
                                    trace_id=ws_push_data.trace_id,
                                    srv_name=data_evt.get('srv_name'),
                                    message=data_evt.get('message'),
                                    error_code=data_evt.get('error_code'))
                        elif ws_push_data.mod_type == sdk_message_pb2.M_MARKETDATA:
                            if self._md_push_handlers is not None and len(self._md_push_handlers) > 0:
                                self._handler_md_data(ws_push_data)
                        elif ws_push_data.mod_type == sdk_message_pb2.M_BASE:
                            if self._base_handlers is not None and len(self._base_handlers) > 0:
                                self._handler_base_data(ws_push_data)
                        elif ws_push_data.mod_type == sdk_message_pb2.M_REPLAYDATA:
                            if self._replay_handlers is not None and len(self._replay_handlers) > 0:
                                self._handler_replay(ws_push_data)
                        elif ws_push_data.mod_type == sdk_message_pb2.M_FACTOR:
                            if self._factor_handlers is not None and len(self._factor_handlers) > 0:
                                self._handler_factor_data(ws_push_data)
                        else:
                            log.warning("[推送数据异常]-未处理的数据类型=%s, data=%s", ws_push_data.mod_type,
                                        ws_push_data)
                            continue
                    else:
                        log.info('[推送数据异常]-未处理的消息=%s', ws_push_data)
                except queue.Empty:
                    time.sleep(0.001)
            log.info('PushDataQueueThread stopped')

        def _handler_base_data(self, ws_push_data):
            """
            基础数据消息处理
            """
            _data = ws_push_data.data
            data_type, data_evt, error = proto_utils.parse_any_obj(_data)
            if data_evt is None and error is None:
                log.error(
                    '[处理推送数据]异常-推送数据及提示为空, trace_id=%s, data_evt=%s, error=%s',
                    ws_push_data.trace_id, data_evt, error)
                return
            for _handler in self._base_handlers:
                if data_type == sdk_message_pb2.UserConnectedReply:
                    _handler.on_user_report(data_evt, error)
                else:
                    log.warning(
                        '[处理推送数据]异常-未处理的基础数据类型, data_type=%s, trace_id=%s, data_evt=%s, error=%s',
                        data_type, ws_push_data.trace_id, data_evt, error)

        def _handler_md_data(self, ws_push_data):
            """
            行情数据消息处理
            """
            _data = ws_push_data.data
            data_type, data_evt, error = proto_utils.parse_any_obj(_data)
            if data_evt is None and error is None:
                log.error(
                    '[实时行情数据处理]异常-推送数据及提示为空, trace_id=%s, data_evt=%s, error=%s',
                    ws_push_data.trace_id, data_evt, error)
                return
            for _handler in self._md_push_handlers:
                if data_type == market_data_pb2.Snapshot:
                    _handler.on_snapshot(data=data_evt, error=error, timestamps=ws_push_data.timestamps)
                elif data_type == market_data_pb2.TickExecution:
                    _handler.on_execution(data_evt, error)
                elif data_type == market_data_pb2.TickOrders:
                    _handler.on_order(data_evt, error)
                elif data_type == market_data_pb2.OrderQueue:
                    _handler.on_orderqueue(data_evt, error)
                elif data_type == market_data_pb2.kLine:
                    _handler.on_kline(data_evt, error)
                elif data_type == market_data_pb2.Index:
                    _handler.on_index(data_evt, error)
                elif data_type == real_time_md_pb2.SubStatus:
                    _handler.on_subscribe_res(data_evt, error)
                else:
                    log.warning(
                        '[实时行情数据处理]异常-未处理的行情数据类型, data_type=%s, trace_id=%s, data_evt=%s, error=%s',
                        data_type, ws_push_data.trace_id, data_evt, error)

        def _handler_replay(self, ws_push_data):
            """
            行情数据消息处理
            """
            _data = ws_push_data.data
            data_type, data_evt, error = proto_utils.parse_any_obj(_data)
            if data_evt is None and error is None:
                log.error(
                    '[数据回放处理]异常-推送数据及提示为空, trace_id=%s, data_evt=%s, error=%s',
                    ws_push_data.trace_id, data_evt, error)
                return
            for _handler in self._replay_handlers:
                if data_type == market_data_pb2.Snapshot:
                    _handler.on_snapshot(data=data_evt, error=error, timestamps=ws_push_data.timestamps)
                elif data_type == market_data_pb2.TickExecution:
                    _handler.on_execution(data_evt, error)
                elif data_type == market_data_pb2.TickOrders:
                    _handler.on_order(data_evt, error)
                elif data_type == market_data_pb2.OrderQueue:
                    _handler.on_orderqueue(data_evt, error)
                elif data_type == market_data_pb2.kLine:
                    _handler.on_kline(data_evt, error)
                elif data_type == market_data_pb2.Index:
                    _handler.on_index(data_evt, error)
                else:
                    log.warning(
                        '[数据回放处理]异常-未处理的数据回放类型, data_type=%s, trace_id=%s, data_evt=%s, error=%s',
                        data_type, ws_push_data.trace_id, data_evt, error)

        def _handler_factor_data(self, ws_push_data):
            """
            行情数据消息处理
            """
            _data = ws_push_data.data
            data_type, data_evt, error = proto_utils.parse_any_obj(_data)
            if data_evt is None and error is None:
                log.error(
                    '[实时行情数据处理]异常-推送数据及提示为空, trace_id=%s, data_evt=%s, error=%s',
                    ws_push_data.trace_id, data_evt, error)
                return
            for _handler in self._factor_handlers:
                if data_type == realtime_factor_data_pb2.RTFactor:
                    # TODO
                    _handler.on_factor(data=data_evt, error=error)
                elif data_type == real_time_md_pb2.SubStatus:
                    _handler.on_factor_sub_res(data_evt, error)
                else:
                    log.warning(
                        '[实时行情数据处理]异常-未处理的行情数据类型, data_type=%s, trace_id=%s, data_evt=%s, error=%s',
                        data_type, ws_push_data.trace_id, data_evt, error)
