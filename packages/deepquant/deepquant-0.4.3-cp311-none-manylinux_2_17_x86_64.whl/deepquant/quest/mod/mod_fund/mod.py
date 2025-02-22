# -*- coding: utf-8 -*-
from typing import Any

from deepquant.quest.const import DEFAULT_ACCOUNT_TYPE, INSTRUMENT_TYPE, RUN_TYPE
from deepquant.quest.core.events import EVENT
from deepquant.quest.data.base_data_source import BaseDataSource
from deepquant.quest.environment import Environment
from deepquant.quest.interface import AbstractMod
from deepquant.quest.utils.logger import system_log
from deepquant.quest.datac.share.errors import PermissionDenied

from deepquant.quest.mod.mod_fund.data import (
    FundInstrumentStore, RqdataFundDayBarStore, RqdataFundDividendStore, RqdataFundSplitStore
)
from deepquant.quest.mod.mod_fund.transaction import FundTransactionDecider


class FundMod(AbstractMod):
    def __init__(self):
        self._fund_day_bar_store = None
        self._fund_dividend_store = None
        self._fund_instrument_store = None
        self._fund_split_store = None

    def _register_dummy_data_stores(self, e):
        # 有回测权限但是没有rqdata的基金权限的时候提示用户没有权限
        from . import dummy
        dummy.PERMISSION_ERROR = e
        self._fund_day_bar_store = dummy.DummyDayBarStore()
        self._fund_dividend_store = dummy.DummyDividendStore()
        self._fund_instrument_store = dummy.DummyInstrumentStore()
        self._fund_split_store = dummy.DummySplitStore()

    def start_up(self, env, mod_config):
        # type: (Environment, Any) -> None

        # 检查回测
        if env.config.base.run_type != RUN_TYPE.BACKTEST:
            system_log.info("yhalpha_mod_fund 当前只支持回测,mod关闭 ")
            return

        # 检查stock账户
        if DEFAULT_ACCOUNT_TYPE.STOCK not in env.config.base.accounts:
            system_log.debug("stock account has not been set, yhalpha_mod_fund disabled")
            return

        from deepquant.quest.mod.mod_fund import api
        env.event_bus.add_listener(EVENT.POST_SYSTEM_INIT, api.init_fund_api)
        try:
            # 权限
            # CHECK_RQSDK_PERMISSION: rqsdk__mod_fund
            pass
        except PermissionError as e:
            self._register_dummy_data_stores(e)
        else:
            # api 导入
            # noinspection PyUnresolvedReferences
            try:
                self._fund_day_bar_store = RqdataFundDayBarStore(mod_config.fund_nav_type)
                self._fund_instrument_store = FundInstrumentStore()
                self._fund_dividend_store = RqdataFundDividendStore()
                self._fund_split_store = RqdataFundSplitStore()
            except PermissionDenied as e:
                # Not permit to run rqdata
                self._register_dummy_data_stores(e)

        # 持仓导入
        # noinspection PyUnresolvedReferences
        from deepquant.quest.mod.mod_fund import position

        # 数据导入
        data_source = env.data_source
        if not data_source:
            bundle_path = env.config.base.data_bundle_path
            custom_future_info = getattr(env.config.base, "future_info", {})
            data_source = BaseDataSource(
                bundle_path,
                custom_future_info,
                DEFAULT_ACCOUNT_TYPE.FUTURE in env.config.base.accounts and env.config.base.futures_time_series_trading_parameters,
                env.config.base.end_date
            )
            env.set_data_source(data_source)

        # data
        data_source.register_instruments_store(self._fund_instrument_store)
        data_source.register_day_bar_store(INSTRUMENT_TYPE.PUBLIC_FUND, self._fund_day_bar_store)
        data_source.register_dividend_store(INSTRUMENT_TYPE.PUBLIC_FUND, self._fund_dividend_store)
        data_source.register_split_store(INSTRUMENT_TYPE.PUBLIC_FUND, self._fund_split_store)

        env.set_transaction_cost_decider(INSTRUMENT_TYPE.PUBLIC_FUND, FundTransactionDecider())

        from .matcher import FundMatcher
        from deepquant.quest.mod.yhalpha_mod_sys_simulation.simulation_broker import SimulationBroker
        broker = env.broker or SimulationBroker(env, env.config.mod.sys_simulation)
        if isinstance(broker, SimulationBroker):
            broker.register_matcher(INSTRUMENT_TYPE.PUBLIC_FUND, FundMatcher(env, mod_config.subscription_limit))
            env.set_broker(broker)

        if mod_config.status_limit:
            from .validator import FundStatusValidator
            env.add_frontend_validator(FundStatusValidator(env), INSTRUMENT_TYPE.PUBLIC_FUND)

    def tear_down(self, code, exception=None):
        pass

    def get_bars(self, market_code):
        return self._fund_day_bar_store.get_bars(market_code)
