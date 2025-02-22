# -*- coding: utf-8 -*-
#

'''
更多描述请见
https://www.ricequant.com/api/python/chn
'''


from deepquant.quest.const import EXECUTION_PHASE
from deepquant.quest.core.execution_context import ExecutionContext
from deepquant.quest.utils.arg_checker import apply_rules, verify_that
import deepquant.quest.datac as yhdatac

from deepquant.quest import export_as_api


_history_cache = {}

_history_warning_fired = False

VALID_NAV_FIELDS = [
    'acc_net_value', 'unit_net_value', 'subscribe_status', 'redeem_status', 'change_rate'
]


@export_as_api
class fund:
    pass


@ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT,
                                EXECUTION_PHASE.BEFORE_TRADING,
                                EXECUTION_PHASE.ON_BAR,
                                EXECUTION_PHASE.AFTER_TRADING,
                                EXECUTION_PHASE.SCHEDULED)
@apply_rules(verify_that('date').is_valid_date(ignore_none=True))
def _fund_all_instruments(date=None):
    return yhdatac.fund.all_instruments(date)


@ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT,
                                EXECUTION_PHASE.BEFORE_TRADING,
                                EXECUTION_PHASE.ON_BAR,
                                EXECUTION_PHASE.AFTER_TRADING,
                                EXECUTION_PHASE.SCHEDULED)
@apply_rules(verify_that('market_code').is_instance_of((str, list)))
def _fund_instruments(market_code):
    return yhdatac.fund.instruments(market_code)


@ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT,
                                EXECUTION_PHASE.BEFORE_TRADING,
                                EXECUTION_PHASE.ON_BAR,
                                EXECUTION_PHASE.AFTER_TRADING,
                                EXECUTION_PHASE.SCHEDULED)
@apply_rules(verify_that('market_code').is_instance_of(str),
             verify_that('date').is_valid_date(ignore_none=True))
def _fund_get_holdings(market_code, date=None):
    return yhdatac.fund.get_holdings(market_code, date)


@ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT,
                                EXECUTION_PHASE.BEFORE_TRADING,
                                EXECUTION_PHASE.ON_BAR,
                                EXECUTION_PHASE.AFTER_TRADING,
                                EXECUTION_PHASE.SCHEDULED)
@apply_rules(verify_that('market_code').is_instance_of(str),
             verify_that('date').is_valid_date(ignore_none=True))
def _fund_get_asset_allocation(market_code, date=None):
    return yhdatac.fund.get_asset_allocation(market_code, date)


@ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT,
                                EXECUTION_PHASE.BEFORE_TRADING,
                                EXECUTION_PHASE.ON_BAR,
                                EXECUTION_PHASE.AFTER_TRADING,
                                EXECUTION_PHASE.SCHEDULED)
@apply_rules(verify_that('market_code').is_instance_of(str))
def _fund_get_dividend(market_code):
    return yhdatac.fund.get_dividend(market_code)


@ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT,
                                EXECUTION_PHASE.BEFORE_TRADING,
                                EXECUTION_PHASE.ON_BAR,
                                EXECUTION_PHASE.AFTER_TRADING,
                                EXECUTION_PHASE.SCHEDULED)
@apply_rules(verify_that('market_code').is_instance_of(str))
def _fund_get_split(market_code):
    return yhdatac.fund.get_split(market_code)


@ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT,
                                EXECUTION_PHASE.BEFORE_TRADING,
                                EXECUTION_PHASE.ON_BAR,
                                EXECUTION_PHASE.AFTER_TRADING,
                                EXECUTION_PHASE.SCHEDULED)
@apply_rules(verify_that('market_code').is_instance_of((str, list)))
def _fund_get_manager(market_code):
    return yhdatac.fund.get_manager(market_code)


@ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT,
                                EXECUTION_PHASE.BEFORE_TRADING,
                                EXECUTION_PHASE.ON_BAR,
                                EXECUTION_PHASE.AFTER_TRADING,
                                EXECUTION_PHASE.SCHEDULED)
@apply_rules(verify_that('market_code').is_instance_of((str, list)),
             verify_that('start_date').is_valid_date(ignore_none=True),
             verify_that('end_date').is_valid_date(ignore_none=True),
             verify_that('fields').are_valid_fields(VALID_NAV_FIELDS, ignore_none=True))
def _fund_get_nav(market_code, start_date=None, end_date=None, fields=None):
    return yhdatac.fund.get_nav(market_code, start_date, end_date, fields)


@ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT,
                                EXECUTION_PHASE.BEFORE_TRADING,
                                EXECUTION_PHASE.ON_BAR,
                                EXECUTION_PHASE.AFTER_TRADING,
                                EXECUTION_PHASE.SCHEDULED)
@apply_rules(verify_that('market_code').is_instance_of(str),
             verify_that('date').is_valid_date(ignore_none=True))
def _fund_get_ratings(market_code, date=None):
    return yhdatac.fund.get_ratings(market_code, date)


@ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT,
                                EXECUTION_PHASE.BEFORE_TRADING,
                                EXECUTION_PHASE.ON_BAR,
                                EXECUTION_PHASE.AFTER_TRADING,
                                EXECUTION_PHASE.SCHEDULED)
@apply_rules(verify_that('market_code').is_instance_of(str),
             verify_that('date').is_valid_date(ignore_none=True))
def _fund_get_units_change(market_code, date=None):
    return yhdatac.fund.get_units_change(market_code, date)


fund.all_instruments = staticmethod(_fund_all_instruments)
fund.instruments = staticmethod(_fund_instruments)
fund.get_holdings = staticmethod(_fund_get_holdings)
fund.get_asset_allocation = staticmethod(_fund_get_asset_allocation)
fund.get_dividend = staticmethod(_fund_get_dividend)
fund.get_split = staticmethod(_fund_get_split)
fund.get_manager = staticmethod(_fund_get_manager)
fund.get_nav = staticmethod(_fund_get_nav)
fund.get_ratings = staticmethod(_fund_get_ratings)
fund.get_units_change = staticmethod(_fund_get_units_change)
