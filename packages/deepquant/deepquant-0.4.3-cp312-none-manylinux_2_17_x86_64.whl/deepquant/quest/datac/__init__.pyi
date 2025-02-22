import deepquant.quest.datac as yhdatac
import deepquant.quest.datac.client
from .client import initialized


__version__: str = ...
init = deepquant.quest.datac.client.init
reset = deepquant.quest.datac.client.reset
initialized = deepquant.quest.datac.client.initialized
concept_list = yhdatac.services.concept.concept_list
concept = yhdatac.services.stock_status.concept
concept_names = yhdatac.services.concept.concept_names
shenwan_industry = yhdatac.services.shenwan.shenwan_industry
shenwan_instrument_industry = yhdatac.services.shenwan.shenwan_instrument_industry
zx_industry = yhdatac.services.shenwan.zx_industry
zx_instrument_industry = yhdatac.services.shenwan.zx_instrument_industry
get_industry = yhdatac.services.stock_status.get_industry
get_instrument_industry = yhdatac.services.shenwan.get_instrument_industry
get_industry_mapping = yhdatac.services.shenwan.get_industry_mapping
industry_code = yhdatac.services.constant.IndustryCode
IndustryCode = yhdatac.services.constant.IndustryCode
sector_code = yhdatac.services.constant.SectorCode
SectorCode = yhdatac.services.constant.SectorCode
get_trading_dates = yhdatac.services.calendar.get_trading_dates
get_next_trading_date = yhdatac.services.calendar.get_next_trading_date
get_previous_trading_date = yhdatac.services.calendar.get_previous_trading_date
get_latest_trading_date = yhdatac.services.calendar.get_latest_trading_date
trading_date_offset = yhdatac.services.calendar.trading_date_offset
is_trading_date = yhdatac.services.calendar.is_trading_date
has_night_trading = yhdatac.services.calendar.has_night_trading
current_trading_date = yhdatac.services.calendar.current_trading_date
id_convert = yhdatac.services.basic.id_convert
get_tick_size = yhdatac.services.basic.get_tick_size
instruments = yhdatac.services.basic.instruments
all_instruments = yhdatac.services.basic.all_instruments
sector = yhdatac.services.basic.sector
industry = yhdatac.services.basic.industry
get_future_contracts = yhdatac.services.basic.get_future_contracts
get_spot_benchmark_price = yhdatac.services.basic.get_spot_benchmark_price
get_stock_connect_holding_details = yhdatac.services.get_price.get_stock_connect_holding_details
get_buy_back = yhdatac.services.market_data.get_buy_back
get_suspend_days = yhdatac.services.stock_status.get_suspend_days


class futures:
    get_commission_margin = yhdatac.services.future.get_commission_margin
    get_contracts = yhdatac.services.basic.get_contracts
    get_dominant = yhdatac.services.future.get_dominant
    get_dominant_price = yhdatac.services.future.get_dominant_price
    get_member_rank = yhdatac.services.future.get_member_rank
    get_warehouse_stocks = yhdatac.services.future.get_warehouse_stocks
    get_contract_multiplier = yhdatac.services.future.get_contract_multiplier
    get_ex_factor = yhdatac.services.future.get_ex_factor
    get_current_basis = yhdatac.services.future.get_current_basis
    get_trading_parameters = yhdatac.services.future.get_trading_parameters


jy_instrument_industry = yhdatac.services.basic.jy_instrument_industry


class econ:
    get_factors = yhdatac.services.basic.get_factors
    get_money_supply = yhdatac.services.basic.get_money_supply
    get_reserve_ratio = yhdatac.services.basic.get_reserve_ratio


get_main_shareholder = yhdatac.services.basic.get_main_shareholder
get_current_news = yhdatac.services.basic.get_current_news
get_trading_hours = yhdatac.services.basic.get_trading_hours
get_private_placement = yhdatac.services.basic.get_private_placement
get_share_transformation = yhdatac.services.basic.get_share_transformation


class user:
    get_quota = yhdatac.services.basic.get_quota


get_update_status = yhdatac.services.basic.get_update_status
info = yhdatac.services.basic.info
get_basic_info = yhdatac.services.basic.get_basic_info


class convertible:
    all_instruments = yhdatac.services.convertible.all_instruments
    get_call_info = yhdatac.services.convertible.get_call_info
    get_cash_flow = yhdatac.services.convertible.get_cash_flow
    get_conversion_info = yhdatac.services.convertible.get_conversion_info
    get_conversion_price = yhdatac.services.convertible.get_conversion_price
    get_credit_rating = yhdatac.services.convertible.get_credit_rating
    get_indicators = yhdatac.services.convertible.get_indicators
    get_industry = yhdatac.services.convertible.get_industry
    get_instrument_industry = yhdatac.services.convertible.get_instrument_industry
    get_latest_rating = yhdatac.services.convertible.get_latest_rating
    get_put_info = yhdatac.services.convertible.get_put_info
    instruments = yhdatac.services.convertible.instruments
    is_suspended = yhdatac.services.convertible.is_suspended
    rating = yhdatac.services.convertible.rating


get_dominant_future = yhdatac.services.future.get_dominant_future
future_commission_margin = yhdatac.services.future.future_commission_margin
get_future_member_rank = yhdatac.services.future.get_future_member_rank
current_stock_connect_quota = yhdatac.services.stock_status.current_stock_connect_quota
get_stock_connect_quota = yhdatac.services.stock_status.get_stock_connect_quota
is_st_stock = yhdatac.services.stock_status.is_st_stock
_is_st_stock = yhdatac.services.stock_status._is_st_stock
is_suspended = yhdatac.services.stock_status.is_suspended
get_stock_connect = yhdatac.services.stock_status.get_stock_connect
get_securities_margin = yhdatac.services.stock_status.get_securities_margin
get_investor_ra = yhdatac.services.stock_status.get_investor_ra
get_margin_stocks = yhdatac.services.stock_status.get_margin_stocks
get_shares = yhdatac.services.stock_status.get_shares
get_allotment = yhdatac.services.stock_status.get_allotment
get_symbol_change_info = yhdatac.services.stock_status.get_symbol_change_info
get_special_treatment_info = yhdatac.services.stock_status.get_special_treatment_info
get_restricted_shares = yhdatac.services.stock_status.get_restricted_shares

current_snapshot = yhdatac.services.live.current_snapshot
get_ticks = yhdatac.services.live.get_ticks
current_minute = yhdatac.services.live.current_minute
get_live_ticks = yhdatac.services.live.get_live_ticks
get_price = yhdatac.services.get_price.get_price
LiveMarketDataClient = yhdatac.services.live_md_client.LiveMarketDataClient
AsyncLiveMarketDataClient = yhdatac.services.async_live_md_client.AsyncLiveMarketDataClient
get_all_factor_names = yhdatac.services.factor.get_all_factor_names
calc_factor = yhdatac.services.factor.calc_factor
get_factor = yhdatac.services.factor.get_factor
get_factor_return = yhdatac.services.factor.get_factor_return
get_factor_exposure = yhdatac.services.factor.get_factor_exposure
get_style_factor_exposure = yhdatac.services.factor.get_style_factor_exposure
get_descriptor_exposure = yhdatac.services.factor.get_descriptor_exposure
get_stock_beta = yhdatac.services.factor.get_stock_beta
get_factor_covariance = yhdatac.services.factor.get_factor_covariance
get_specific_return = yhdatac.services.factor.get_specific_return
get_specific_risk = yhdatac.services.factor.get_specific_risk
get_index_factor_exposure = yhdatac.services.factor.get_index_factor_exposure
get_pit_financials_ex = yhdatac.services.financial.get_pit_financials_ex
current_performance = yhdatac.services.financial.current_performance
performance_forecast = yhdatac.services.financial.performance_forecast
get_capital_flow = yhdatac.services.get_capital_flow.get_capital_flow
current_capital_flow_minute = yhdatac.services.get_capital_flow.current_capital_flow_minute
get_open_auction_info = yhdatac.services.get_capital_flow.get_open_auction_info
get_close_auction_info = yhdatac.services.get_capital_flow.get_close_auction_info
index_components = yhdatac.services.index.index_components
index_weights = yhdatac.services.index.index_weights
index_indicator = yhdatac.services.index.index_indicator
index_weights_ex = yhdatac.services.index.index_weights_ex
get_ksh_auction_info = yhdatac.services.ksh_auction_info.get_ksh_auction_info
get_split = yhdatac.services.market_data.get_split
get_dividend = yhdatac.services.market_data.get_dividend
get_dividend_info = yhdatac.services.market_data.get_dividend_info
get_ex_factor = yhdatac.services.market_data.get_ex_factor
get_turnover_rate = yhdatac.services.market_data.get_turnover_rate
get_price_change_rate = yhdatac.services.market_data.get_price_change_rate
get_yield_curve = yhdatac.services.market_data.get_yield_curve
get_block_trade = yhdatac.services.market_data.get_block_trade
get_exchange_rate = yhdatac.services.market_data.get_exchange_rate
get_temporary_code = yhdatac.services.market_data.get_temporary_code
get_interbank_offered_rate = yhdatac.services.market_data.get_interbank_offered_rate


class options:
    get_contract_property = yhdatac.services.options.get_contract_property
    get_contracts = yhdatac.services.options.get_contracts
    get_greeks = yhdatac.services.options.get_greeks


class fenji:
    get = yhdatac.services.structured_fund.get
    get_a_by_interest_rule = yhdatac.services.structured_fund.get_a_by_interest_rule
    get_a_by_yield = yhdatac.services.structured_fund.get_a_by_yield
    get_all = yhdatac.services.structured_fund.get_all


ecommerce = yhdatac.services.tmall.ecommerce


class xueqiu:
    history = yhdatac.services.xueqiu.history
    top_stocks = yhdatac.services.xueqiu.top_stocks


class consensus:
    get_indicator = yhdatac.services.consensus.get_indicator
    get_price = yhdatac.services.consensus.get_price
    get_comp_indicators = yhdatac.services.consensus.get_comp_indicators
    all_industries = yhdatac.services.consensus.all_industries
    get_industry_rating = yhdatac.services.consensus.get_industry_rating
    get_market_estimate = yhdatac.services.consensus.get_market_estimate
    get_security_change = yhdatac.services.consensus.get_security_change
    get_expect_appr_exceed = yhdatac.services.consensus.get_expect_appr_exceed
    get_expect_prob = yhdatac.services.consensus.get_expect_prob
    get_factor = yhdatac.services.consensus.get_factor
    get_analyst_momentum = yhdatac.services.consensus.get_analyst_momentum


current_freefloat_turnover = yhdatac.services.extra.current_freefloat_turnover
get_live_minute_price_change_rate = yhdatac.services.extra.get_live_minute_price_change_rate