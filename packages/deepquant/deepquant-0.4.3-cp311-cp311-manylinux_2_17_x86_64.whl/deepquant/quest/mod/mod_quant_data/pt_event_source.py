# -*- coding: utf-8 -*-
import time
import random
from dateutil.parser import parse

import redis
from redis.exceptions import RedisError

from deepquant.quest.interface import AbstractEventSource
from deepquant.quest.environment import Environment
from deepquant.quest.utils import get_trading_period, is_night_trading, is_trading
from deepquant.quest.utils import rq_json as json_utils
from deepquant.quest.utils.logger import system_log
from deepquant.quest.core.events import EVENT, Event

# use system urandom seed
random.seed()


class PTEventSource(AbstractEventSource):
    def __init__(self, redis_url, logger):
        self._redis = redis.from_url(redis_url)
        self._logger = logger
        self._trading_period = None
        self._need_night_trading = False
        self._env = Environment.get_instance()
        self._env.event_bus.add_listener(EVENT.POST_UNIVERSE_CHANGED, self._gen_trading_period)

    def set_state(self, state):
        persist_dict = json_utils.convert_json_to_dict(state.decode('utf-8'))
        self._need_night_trading = persist_dict['_need_night_trading']

    def get_state(self):
        return json_utils.convert_dict_to_json({
            "_need_night_trading": self._need_night_trading,
        }).encode('utf-8')

    def _gen_trading_period(self, *args):
        self._trading_period = get_trading_period(self._env.get_universe(), self._env.config.base.accounts)
        self._need_night_trading = is_night_trading(self._env.get_universe())

    EVENTS = {'bar', 'before_trading', 'after_trading', 'open_auction'}

    @staticmethod
    def _is_valid_event(e):
        splited = e.split()
        if len(splited) != 2 or splited[0] not in PTEventSource.EVENTS:
            return False
        try:
            Environment.get_instance().data_proxy.get_trading_dt(parse(splited[1]))
        except RuntimeError:
            return False

        return True

    @staticmethod
    def _filter_bars(events):
        events = [e for e in events if PTEventSource._is_valid_event(e)]
        if len(events) <= 1:
            return events

        results = []

        def is_bar(e):
            return e.startswith('bar ')

        for i in range(len(events) - 1):
            if not is_bar(events[i]):
                results.append(events[i])
            else:
                if is_bar(events[i + 1]):
                    continue
                else:
                    results.append(events[i])

        results.append(events[-1])

        return results

    # 对 before_trading/after_trading 事件加随机延迟，避免对后端服务造成瞬时冲击
    EVENT_DELAY_MAX = 600

    def events(self, start_date, end_date, frequency):
        self._gen_trading_period()
        if frequency != '1m':
            raise RuntimeError('PT event source support 1m only')

        running = True
        events = []

        def _get_all_msgs(ps):
            while True:
                msg = ps.get_message(ignore_subscribe_messages=True)
                if msg is None:
                    break
                system_log.debug("redis msg {}".format(msg))
                events.append(msg['data'].decode())
            return events

        while running:
            try:
                ps = self._redis.pubsub()
                ps.subscribe('market_event')
                while True:
                    events = _get_all_msgs(ps)
                    events = self._filter_bars(events)

                    for msg in events:
                        system_log.info("Event Source: {}".format(msg))
                        name, dt = msg.split()
                        calendar_dt = parse(dt)
                        night_trading = calendar_dt.hour > 19 or calendar_dt.hour < 4
                        if night_trading and not self._need_night_trading:
                            # 如果当前正在交易夜盘，但是没有subscribe对应的夜盘数据，则不 yield 对应的event
                            continue

                        trading_dt = Environment.get_instance().data_proxy.get_trading_dt(calendar_dt)

                        if name == 'before_trading':
                            time.sleep(random.random() * self.EVENT_DELAY_MAX // 60)
                            yield Event(EVENT.BEFORE_TRADING, calendar_dt=calendar_dt, trading_dt=trading_dt)
                        elif name == 'open_auction':
                            yield Event(EVENT.OPEN_AUCTION, calendar_dt=calendar_dt, trading_dt=trading_dt)
                        elif name == 'after_trading':
                            time.sleep(random.random() * self.EVENT_DELAY_MAX)
                            yield Event(EVENT.AFTER_TRADING, calendar_dt=calendar_dt, trading_dt=trading_dt)
                        elif name == 'bar':
                            if not is_trading(trading_dt, self._trading_period):
                                # 如果当前时间并不在trading_period中，则不执行handle_bar
                                continue
                            yield Event(EVENT.BAR, calendar_dt=calendar_dt, trading_dt=trading_dt)

                    if not running:
                        break

                    events = []
                    msg = ps.get_message(ignore_subscribe_messages=True, timeout=60)
                    if msg is not None:
                        events.append(msg['data'].decode())
            except RedisError as e:
                self._logger.warn('redis error: {}'.format(e))
                time.sleep(3)
