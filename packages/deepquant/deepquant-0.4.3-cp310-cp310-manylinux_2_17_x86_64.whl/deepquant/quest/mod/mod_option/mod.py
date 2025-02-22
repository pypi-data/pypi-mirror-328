# -*- coding: utf-8 -*-
import os
from typing import Any
import numpy as np
from deepquant.quest.const import INSTRUMENT_TYPE, RUN_TYPE, MATCHING_TYPE, DEFAULT_ACCOUNT_TYPE
from deepquant.quest.data.base_data_source import BaseDataSource
from deepquant.quest.environment import Environment
from deepquant.quest.interface import AbstractMod
from deepquant.quest.utils.logger import system_log

from .frontend_validator import OptionValidator
from .transaction_cost_decider import OptionTransactionCostDecider


class OptionMod(AbstractMod):
    def __init__(self):
        self._env = None
        self._dtypes_map = {
            "Option": np.dtype([
                ('datetime', '<i8'),
                ('trading_date', '<i4'),
                ('open', '<f8'),
                ('high', '<f8'),
                ('low', '<f8'),
                ('close', '<f8'),
                ('open_interest', '<i8'),
                ('volume', '<f8'),
                ('total_turnover', '<f8')
            ])
        }

    def start_up(self, env, mod_config):
        # type: (Environment, Any) -> None

        self._env = env
        if env.config.base.run_type != RUN_TYPE.BACKTEST:
            system_log.info("mod_option only support backtest, disabled")
            return

        simulation_config = env.config.mod.sys_simulation
        if simulation_config.signal:
            system_log.warning("mod_option does not support signal mode, disabled")
            return

        try:
            # CHECK_RQSDK_PERMISSION: rqsdk__mod_option
            pass
        except PermissionError as e:
            from . import dummy

            dummy.PERMISSION_ERROR = e
            day_bar_store = dummy.DummyDayBarStore()
            instrument_store = dummy.DummyInstrumentStore()
        else:
            from .data import RQDataDayBarStore, OptionInstrumentStore
            day_bar_store = RQDataDayBarStore()
            instrument_store = OptionInstrumentStore()

            # api
            # noinspection PyUnresolvedReferences
            from . import api

        # position
        # noinspection PyUnresolvedReferences
        from .position import OptionPosition, OptionPositionProxy

        # validator
        env.add_frontend_validator(OptionValidator(env))

        from deepquant.quest.mod.mod_sys_accounts.position_validator import PositionValidator
        env.add_frontend_validator(PositionValidator(), instrument_type=INSTRUMENT_TYPE.OPTION)

        # transaction_cost_decider
        transaction_cost_mod_config = env.config.mod.sys_transaction_cost
        if transaction_cost_mod_config.commission_multiplier is None:
            commission_multiplier = transaction_cost_mod_config.futures_commission_multiplier
        else:
            commission_multiplier = transaction_cost_mod_config.commission_multiplier
        env.set_transaction_cost_decider(INSTRUMENT_TYPE.OPTION, OptionTransactionCostDecider(
            env, commission_multiplier
        ))

        # broker
        from deepquant.quest.mod.mod_sys_simulation.simulation_broker import SimulationBroker
        from .matcher import OptionBarMatcher, OptionTickMatcher, OptionCounterPartyMatcher
        broker = env.broker or SimulationBroker(env, env.config.mod.sys_simulation)
        if not isinstance(broker, SimulationBroker):
            system_log.info("mod_option does not support signal mode, disabled")
            return
        if env.config.base.frequency == "tick":
            option_matcher = OptionTickMatcher
            if env.config.mod.sys_simulation.matching_type == MATCHING_TYPE.COUNTERPARTY_OFFER:
                option_matcher = OptionCounterPartyMatcher
        else:
            option_matcher = OptionBarMatcher

        broker.register_matcher(INSTRUMENT_TYPE.OPTION, option_matcher(env, env.config.mod.sys_simulation))
        env.set_broker(broker)

        # data_source
        data_source = env.data_source or BaseDataSource(
            env.config.base.data_bundle_path,
            getattr(env.config.base, "future_info", {}),
            DEFAULT_ACCOUNT_TYPE.FUTURE in env.config.base.accounts and env.config.base.futures_time_series_trading_parameters,
            env.config.base.end_date
        )
        if not (hasattr(data_source, "register_day_bar_store") and hasattr(data_source, "register_instruments_store")):
            raise RuntimeError("Only support BaseDataSource like data source, current: {]".format(type(data_source)))

        data_source.register_day_bar_store(INSTRUMENT_TYPE.OPTION, day_bar_store)
        data_source.register_instruments_store(instrument_store)
        env.set_data_source(data_source)

        OptionPosition.exercise_slippage = mod_config.exercise_slippage

        if env.config.base.frequency == "1m":
            self._register_minbar_store(data_source)

        # 自定义品种手续费
        if mod_config.commission:
            from .transaction_cost_decider import add_custom_commission
            for underlying_symbol, commission in mod_config.commission.items():
                add_custom_commission(underlying_symbol, commission)

    def tear_down(self, code, exception=None):
        pass

    def _register_minbar_store(self, data_source):

        if not hasattr(data_source, "register_minbar_store"):
            system_log.info("option minbar store disabled, current data source {}".format(data_source))
            return

        try:
            from deepquant.quest.mod.mod_quant_data.data_sources.data_store import H5MinBarStore
        except ImportError:
            system_log.warning("option minbar store disabled, rqalpa_mod_ricequant_data needed")
            return
        try:
            h5_minbar_path = self._env.config.mod.ricequant_data.h5_minbar_path
        except AttributeError:
            h5_minbar_path = None
        default_minbar_path = os.path.join(self._env.config.base.data_bundle_path, "h5")
        minbar_path = os.path.join(h5_minbar_path or default_minbar_path)
        min_bar_store = H5MinBarStore(minbar_path, self._dtypes_map)
        data_source.register_minbar_store(INSTRUMENT_TYPE.OPTION, min_bar_store)
