from typing import Any


from deepquant.quest.const import DEFAULT_ACCOUNT_TYPE, INSTRUMENT_TYPE
from deepquant.quest.data.base_data_source.data_source import BaseDataSource
from deepquant.quest.environment import Environment
from deepquant.quest.interface import AbstractMod
from deepquant.quest.mod.mod_sys_accounts.api.api_future import (future_buy_close, future_buy_open, future_sell_close,
                                                                 future_sell_open)
from deepquant.quest.utils.logger import system_log


class SpotMod(AbstractMod):
    def __init__(self):
        self._env = None

    def start_up(self, env, mod_config):
        self._env = env
        if DEFAULT_ACCOUNT_TYPE.STOCK not in env.config.base.accounts:
            system_log.debug("no stock account, SpotMod disabled.")
            return

        try:
            # CHECK_RQSDK_PERMISSION: rqsdk__mod_spot
            pass
        except PermissionError as e:
            from . import dummy
            dummy.PERMISSION_ERROR = e

            day_bar_store = dummy.DummyDayBarStore()
            instrument_store = dummy.DummyInstrumentStore()
        else:
            from deepquant.quest.apis.api_abstract import buy_close, buy_open, sell_close, sell_open

            # api
            buy_open.register(INSTRUMENT_TYPE.SPOT)(future_buy_open)
            buy_close.register(INSTRUMENT_TYPE.SPOT)(future_buy_close)
            sell_open.register(INSTRUMENT_TYPE.SPOT)(future_sell_open)
            sell_close.register(INSTRUMENT_TYPE.SPOT)(future_sell_close)

            # position
            from . import position

            from .data import SpotDaybarStore, SpotInstrumentStore
            day_bar_store = SpotDaybarStore()
            instrument_store = SpotInstrumentStore()

        # data
        from .data import SpotDaybarStore, SpotInstrumentStore
        data_source = env.data_source or BaseDataSource(
            env.config.base.data_bundle_path,
            getattr(env.config.base, "future_info", {}),
            DEFAULT_ACCOUNT_TYPE.FUTURE in env.config.base.accounts and env.config.base.futures_time_series_trading_parameters,
            env.config.base.end_date
        )
        if not (hasattr(data_source, "register_day_bar_store") and hasattr(data_source, "register_instruments_store")):
            raise RuntimeError("Only support BaseDataSource like data source, current: {}".format(type(data_source)))
        data_source.register_instruments_store(instrument_store)
        data_source.register_day_bar_store(INSTRUMENT_TYPE.SPOT, day_bar_store)
        env.set_data_source(data_source)

        # transaction_cost
        from .transaction_cost import SpotTransactionDecider
        env.set_transaction_cost_decider(INSTRUMENT_TYPE.SPOT, SpotTransactionDecider(
            env, mod_config.commission_multiplier
        ))

        # validator
        from .validator import SpotFrontendValidator
        env.add_frontend_validator(SpotFrontendValidator(), INSTRUMENT_TYPE.SPOT)

    def tear_down(self, code, exception=None):
        pass
