# -*- coding: utf-8 -*-
import os

import deepquant.quest.datac

import numpy as np
from deepquant.quest.const import INSTRUMENT_TYPE, RUN_TYPE, MATCHING_TYPE, DEFAULT_ACCOUNT_TYPE
from deepquant.quest.data.base_data_source import BaseDataSource
from deepquant.quest.interface import AbstractMod
from deepquant.quest.utils.logger import system_log


class ConvertibleMod(AbstractMod):
    def __init__(self):
        self._env = None
        self._dtypes_map = {
            "Convertible": np.dtype([
                ('datetime', '<i8'),
                ('open', '<f8'),
                ('high', '<f8'),
                ('low', '<f8'),
                ('close', '<f8'),
                ('volume', '<f8'),
                ('total_turnover', '<f8'),
            ])
        }

    def start_up(self, env, mod_config):
        self._env = env
        if env.config.base.run_type != RUN_TYPE.BACKTEST:
            system_log.info("yhalpha_mod_convertible only support backtest, disabled")
            return

        try:
            # CHECK_RQSDK_PERMISSION: rqsdk__mod_convertible
            pass
        except PermissionError as e:
            from . import dummy
            dummy.PERMISSION_ERROR = e
            day_bar_store = dummy.DummyDayBarStore()
            instruments_store = dummy.DummyInstrumentStore()
            suspend_date_set = None
        else:
            # noinspection PyUnresolvedReferences
            from . import api
            from .data import ConvertibleInstrumentStore, RQDataDayBarStore, ConvertibleSuspendedDaysDataset

            day_bar_store = RQDataDayBarStore()
            try:
                instruments_store = ConvertibleInstrumentStore()
                instruments_store.get_all_instruments()
            except deepquant.quest.datac.share.errors.PermissionDenied as e:
                from . import dummy
                dummy.PERMISSION_ERROR = e
                instruments_store = dummy.DummyInstrumentStore()
            suspend_date_set = ConvertibleSuspendedDaysDataset()
        # position
        # noinspection PyUnresolvedReferences
        from . import position

        # broker
        from deepquant.quest.mod.mod_sys_simulation.simulation_broker import SimulationBroker
        from .matcher import ConvertibleBarMatcher, ConvertibleTickMatcher, ConvertibleCounterPartyMatcher
        broker = env.broker or SimulationBroker(env, env.config.mod.sys_simulation)
        if not isinstance(broker, SimulationBroker):
            system_log.info("yhalpha_mod_convertible: signal mode enabled, some transaction type may not be supported")
        else:
            if env.config.base.frequency == "tick":
                convertible_matcher = ConvertibleTickMatcher
                if env.config.mod.sys_simulation.matching_type == MATCHING_TYPE.COUNTERPARTY_OFFER:
                    convertible_matcher = ConvertibleCounterPartyMatcher
            else:
                convertible_matcher = ConvertibleBarMatcher

            broker.register_matcher(INSTRUMENT_TYPE.CONVERTIBLE, convertible_matcher(env, env.config.mod.sys_simulation))
            env.set_broker(broker)

        # data source
        data_source = env.data_source or BaseDataSource(
            env.config.base.data_bundle_path, 
            getattr(env.config.base, "future_info", {}),
            DEFAULT_ACCOUNT_TYPE.FUTURE in env.config.base.accounts and env.config.base.futures_time_series_trading_parameters,
            env.config.base.end_date
        )
        if not all((hasattr(data_source, func_name) for func_name in [
            "register_day_bar_store", "register_instruments_store", "append_suspend_date_set"
        ])):
            raise RuntimeError("Only support BaseDataSource like data source, current: {}".format(type(data_source)))
        data_source.register_day_bar_store(INSTRUMENT_TYPE.CONVERTIBLE, day_bar_store)
        data_source.register_instruments_store(instruments_store)
        if suspend_date_set:
            data_source.append_suspend_date_set(suspend_date_set)
        env.set_data_source(data_source)

        # transaction cost decider
        from .transaction import ConvertibleTransactionDecider
        bond_transaction_decider = ConvertibleTransactionDecider(mod_config.commission_rate, mod_config.min_commission)
        env.set_transaction_cost_decider(INSTRUMENT_TYPE.CONVERTIBLE, bond_transaction_decider)

        # validator
        from .validator import ConvertibleValidator
        env.add_frontend_validator(ConvertibleValidator(env))

        if env.config.base.frequency == '1m':
            self._register_minbar_store(data_source)

    def _register_minbar_store(self, data_source):
        # minbar store
        if not hasattr(data_source, "register_minbar_store"):
            system_log.info("convertible minbar store disabled, current data source {}".format(data_source))
            return

        try:
            from deepquant.quest.mod.mod_quant_data.data_sources.data_store import H5MinBarStore
        except ImportError:
            system_log.warning("contertible minbar store disabled, rqalpa_mod_ricequant_data needed")
        else:
            try:
                h5_minbar_path = self._env.config.mod.ricequant_data.h5_minbar_path
            except AttributeError:
                h5_minbar_path = None
            minbar_path = os.path.join(
                h5_minbar_path or os.path.join(self._env.config.base.data_bundle_path, "h5")
            )

            data_source.register_minbar_store(INSTRUMENT_TYPE.CONVERTIBLE, H5MinBarStore(minbar_path, self._dtypes_map))

    def tear_down(self, code, exception=None):
        pass
