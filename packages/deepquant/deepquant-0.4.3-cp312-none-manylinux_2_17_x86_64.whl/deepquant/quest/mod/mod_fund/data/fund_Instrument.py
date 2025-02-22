#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2020/8/7 15:00
# @File    : fund_Instrument.py
import datetime
from collections.abc import Iterable
from itertools import chain
from typing import Optional

import deepquant.quest.datac
from deepquant.quest.const import INSTRUMENT_TYPE
from deepquant.quest.data.base_data_source.storage_interface import AbstractInstrumentStore
from deepquant.quest.model.instrument import Instrument


class FundInstrument(Instrument):
    type = property(lambda self: INSTRUMENT_TYPE.PUBLIC_FUND)
    accrued_daily = property(lambda self: self.__dict__.get("accrued_daily"))
    amc = property(lambda self: self.__dict__.get("amc"))
    amc_id = property(lambda self: self.__dict__.get("amc_id"))
    benchmark = property(lambda self: self.__dict__.get("benchmark"))
    establishment_date = property(lambda self: self.__dict__.get("establishment_date"))
    fund_manager = property(lambda self: self.__dict__.get("fund_manager"))
    fund_type = property(lambda self: self.__dict__.get("fund_type"))
    investment_scope = property(lambda self: self.__dict__.get("investment_scope"))
    issuer = property(lambda self: self.__dict__.get("issuer"))
    latest_size = property(lambda self: self.__dict__.get("latest_size"))
    min_investment = property(lambda self: self.__dict__.get("min_investment"))
    stop_date = property(lambda self: self.__dict__.get("stop_date"))
    transition_time = property(lambda self: self.__dict__.get("transition_time"))
    trustee = property(lambda self: self.__dict__.get("trustee"))
    listed_date = property(lambda self: self.__dict__.get("listed_date"))
    de_listed_date = property(lambda self: self.__dict__.get("de_listed_date"))


class FundInstrumentStore(AbstractInstrumentStore):

    def __init__(self):
        self._all_ins = {i.market_code: i for i in deepquant.quest.datac.fund.instruments(deepquant.quest.datac.fund.all_instruments().market_code)}
        # 基金标的为纯数字组成
        self._sym_id_map = {i.security_name: i.market_code for i in self._all_ins.values()}

    @property
    def all_id_and_syms(self):
        return chain(self._sym_id_map.keys(), self._sym_id_map.values())

    @property
    def instrument_type(self):
        # type: () -> INSTRUMENT_TYPE
        return INSTRUMENT_TYPE.PUBLIC_FUND

    def get_instruments(self, id_or_syms):
        # type: (Optional[Iterable[str]]) -> Iterable[FundInstrument]
        if id_or_syms is None:
            ins_iter = self._all_ins.values()
        else:
            def _iter():
                for id_or_sym in id_or_syms:
                    o = self._sym_id_map[id_or_sym] if id_or_sym in self._sym_id_map else id_or_sym
                    if o in self._all_ins:
                        yield self._all_ins[o]
            ins_iter = _iter()
        for ins in ins_iter:
            ins_dict = ins.__dict__.copy()
            if not ins_dict["listed_date"]:
                ins_dict["listed_date"] = datetime.datetime(1999, 1, 1)
            if not ins_dict["de_listed_date"]:
                ins_dict["de_listed_date"] = datetime.datetime(2999, 12, 31)
            ins_dict["accrued_daily"] = bool(getattr(ins, "accrued_daily", False) or getattr(ins, "accrued_type", None))
            yield FundInstrument(ins_dict)
