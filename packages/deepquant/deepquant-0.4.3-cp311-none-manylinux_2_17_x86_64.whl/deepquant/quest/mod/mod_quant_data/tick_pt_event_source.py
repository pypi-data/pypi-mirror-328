import time
import random
import json
import datetime
from functools import lru_cache
from collections import defaultdict
from redis.exceptions import RedisError
from dateutil.parser import parse
from six import iteritems

from deepquant.quest.utils import is_trading
from deepquant.quest.environment import Environment
from deepquant.quest.model.tick import TickObject
from deepquant.quest.utils.logger import system_log
from deepquant.quest.core.events import EVENT, Event
from deepquant.quest.utils.datetime_func import convert_ms_int_to_datetime
from deepquant.quest.utils import TimeRange
import deepquant.quest.datac as yhdatac

from deepquant.quest.mod.mod_quant_data.pt_event_source import PTEventSource

random.seed()


def convert_int_to_datetime_with_ms(dt_int):
    dt_int = int(dt_int)
    year, r = divmod(dt_int, 10000000000000)
    month, r = divmod(r, 100000000000)
    day, r = divmod(r, 1000000000)
    hour, r = divmod(r, 10000000)
    minute, r = divmod(r, 100000)
    second, millisecond = divmod(r, 1000)

    return datetime.datetime(year, month, day, hour, minute, second, millisecond * 1000)


@lru_cache()
def get_tick_trading_period(market_code):
    # noinspection PyUnresolvedReferences
    trading_hours = yhdatac.get_trading_hours(market_code, frequency="tick")
    trading_period = []
    trading_hours = trading_hours.replace("-", ":")
    for time_range_str in trading_hours.split(","):
        start_h, start_m, end_h, end_m = (int(i) for i in time_range_str.split(":"))
        start, end = datetime.time(start_h, start_m), datetime.time(end_h, end_m)
        if start > end:
            trading_period.append(TimeRange(start, datetime.time(23, 59)))
            trading_period.append(TimeRange(datetime.time(0, 0), end))
        else:
            trading_period.append(TimeRange(start, end))
    return trading_period


class TickPtEventSource(PTEventSource):
    def __init__(self, bar_redis_url, logger):
        super(TickPtEventSource, self).__init__(bar_redis_url, logger)
        self._tick_redis = self._redis
        self._bar_redis = self._redis
        self._env.system_log.debug('You are using tick pt event source')

    @staticmethod
    def _filter_ticks(events):
        return {market_code: msgs[-1] for market_code, msgs in iteritems(events)}

    EVENT_DELAY_MAX = 600

    @staticmethod
    def _convert_tick_datetime(date, time):
        year, r = divmod(date, 10000)
        month, day = divmod(r, 100)
        hour, r = divmod(time, 10000000)
        minute, r = divmod(r, 100000)
        second, millisecond = divmod(r, 1000)
        return datetime.datetime(year, month, day, hour, minute, second, millisecond * 1000)

    def events(self, start_date, end_date, frequency):
        self._gen_trading_period()
        if frequency != 'tick':
            raise RuntimeError('Tick event source support tick only')

        running = True

        def _get_all_bar_msgs(ps):
            events = []

            msg = ps.get_message(ignore_subscribe_messages=True, timeout=0.01)
            if msg is None:
                return events
            system_log.debug("redis msg {}".format(msg))
            events.append(msg['data'].decode())

            while True:
                msg = ps.get_message(ignore_subscribe_messages=True)
                if msg is None:
                    break
                system_log.debug("redis msg {}".format(msg))
                events.append(msg['data'].decode())
            return events

        def _get_all_tick_msgs(ps):
            events = defaultdict(list)

            msg = ps.get_message(ignore_subscribe_messages=True, timeout=0.1)
            if msg is None:
                return events
            system_log.debug("redis msg {}".format(msg))
            events[msg['channel'].decode()].append(msg['data'].decode())

            while True:
                msg = ps.get_message(ignore_subscribe_messages=True)
                if msg is None:
                    break
                system_log.debug("redis msg {}".format(msg))
                events[msg['channel'].decode()].append(msg['data'].decode())
            return events

        def _redis_tick_key(market_code):
            return 'tick_{}'.format(market_code)

        while running:
            try:
                bar_ps = self._bar_redis.pubsub()
                bar_ps.subscribe('market_event')

                should_get_tick = False

                tick_ps = self._tick_redis.pubsub()
                origin_universe = self._env.get_universe()
                for market_code in self._env.get_universe():
                    should_get_tick = True
                    tick_ps.subscribe(_redis_tick_key(market_code))

                while True:
                    # 获取 before_trading、after_trading 事件
                    bar_events = _get_all_bar_msgs(bar_ps)
                    bar_events = PTEventSource._filter_bars(bar_events)

                    for msg in bar_events:
                        name, dt = msg.split()
                        calendar_dt = parse(dt)
                        night_trading = calendar_dt.hour > 19 or calendar_dt.hour < 4
                        if night_trading and not self._need_night_trading:
                            # 如果当前正在交易夜盘，但是没有subscribe对应的夜盘数据，则不 yield 对应的event
                            continue
                        trading_dt = Environment.get_instance().data_proxy.get_trading_dt(calendar_dt)

                        if name == 'before_trading':
                            yield Event(EVENT.BEFORE_TRADING, calendar_dt=calendar_dt, trading_dt=trading_dt)
                        elif name == 'after_trading':
                            # time.sleep(random.random() * self.EVENT_DELAY_MAX)
                            yield Event(EVENT.AFTER_TRADING, calendar_dt=calendar_dt, trading_dt=trading_dt)
                        elif name == 'bar':
                            if not is_trading(trading_dt, self._trading_period):
                                # 如果当前时间并不在trading_period中，则不执行handle_bar
                                continue
                            yield Event(EVENT.BAR, calendar_dt=calendar_dt, trading_dt=trading_dt)

                    if should_get_tick:
                        tick_events = _get_all_tick_msgs(tick_ps)
                        tick_events = TickPtEventSource._filter_ticks(tick_events)
                    else:
                        tick_events = {}
                    for event_name, msg in iteritems(tick_events):
                        market_code = event_name[5:]
                        tick_dict = json.loads(msg)

                        try:
                            calendar_dt = self._convert_tick_datetime(tick_dict['date'], tick_dict["time"])
                        except KeyError:
                            calendar_dt = convert_ms_int_to_datetime(tick_dict["datetime"])
                        trading_dt = Environment.get_instance().data_proxy.get_trading_dt(calendar_dt)

                        trading_period = get_tick_trading_period(market_code)
                        if not is_trading(calendar_dt, trading_period):
                            continue
                        # 过滤stock集合竞价时间
                        if (
                            market_code.endswith(".SE") or market_code.endswith(".SH")
                        ) and (
                            datetime.time(14, 57) <= calendar_dt.time() <= datetime.time(15, 0)
                        ):
                            continue

                        tick_dict["datetime"] = calendar_dt
                        if "asks" not in tick_dict:
                            tick_dict["asks"] = tick_dict.get("ask", [])
                        if "bids" not in tick_dict:
                            tick_dict["bids"] = tick_dict.get("bid", [])
                        if "ask_vols" not in tick_dict:
                            tick_dict["ask_vols"] = tick_dict.get("ask_vol", [])
                        if "bid_vols" not in tick_dict:
                            tick_dict["bid_vols"] = tick_dict.get("bid_vol", [])

                        yield Event(EVENT.TICK, calendar_dt=calendar_dt, trading_dt=trading_dt, tick=TickObject(
                            Environment.get_instance().data_proxy.instruments(market_code), tick_dict
                        ))

                    if not running:
                        break

                    # 重新处理订阅
                    new_universe = self._env.get_universe()
                    if len(new_universe) > 0:
                        should_get_tick = True
                    else:
                        should_get_tick = False

                    for obid in origin_universe - new_universe:
                        tick_ps.unsubscribe(_redis_tick_key(obid))
                    for obid in new_universe - origin_universe:
                        tick_ps.subscribe(_redis_tick_key(obid))

            except RedisError as e:
                self._logger.warn('redis error: {}'.format(e))
                time.sleep(3)
