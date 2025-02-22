#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2020/4/28 20:32
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : mod.py
import os
import shutil

from deepquant.quest.const import DEFAULT_ACCOUNT_TYPE
from deepquant.quest.const import RUN_TYPE
from deepquant.quest.interface import AbstractMod


class RicequantDataMod(AbstractMod):
    def __init__(self):
        pass

    def start_up(self, env, mod_config):
        bundle_path = env.config.base.data_bundle_path
        tick_path = os.path.join(bundle_path, "h5", "ticks")
        if os.path.exists(tick_path):
            if os.path.exists(os.path.join(bundle_path, "ticks")):
                shutil.rmtree(os.path.join(bundle_path, "ticks"))
            shutil.move(tick_path, bundle_path)

        if env.config.base.run_type == RUN_TYPE.BACKTEST:
            if DEFAULT_ACCOUNT_TYPE.STOCK in env.config.base.accounts:
                # CHECK_RQSDK_PERMISSION: rqsdk__mod_backtest_stock
                pass
            if DEFAULT_ACCOUNT_TYPE.FUTURE in env.config.base.accounts:
                # CHECK_RQSDK_PERMISSION: rqsdk__mod_backtest_future
                pass

            from .data_sources import BundleDataSource
            env.set_data_source(BundleDataSource(
                env.config.base.data_bundle_path, 
                mod_config.h5_minbar_path, 
                mod_config.h5_tick_path,
                tick_type=mod_config.tick_type, 
                custom_future_info=env.config.base.future_info,
            ))

            if env.config.base.frequency == 'tick':
                from .tick_price_board import TickPriceBoard
                # FIXME: dirty hack
                env.price_board = TickPriceBoard(None)

            if env.config.base.frequency == "1m":
                from .minute_price_board import MinutePriceBoard
                env.price_board = MinutePriceBoard()

        else:
            from .data_sources import PTDataSource
            from .redis_store import RedisStore

            redis_store = RedisStore(mod_config.redis_url)
            env.set_data_source(PTDataSource(redis_store, env.config.base.future_info))

            if env.config.base.frequency == '1m':
                from .snapshot_price_board import SnapshotPriceBoard
                env.set_price_board(SnapshotPriceBoard(env))

                if env.config.base.run_type == RUN_TYPE.PAPER_TRADING:
                    from .pt_event_source import PTEventSource
                    env.set_event_source(PTEventSource(mod_config.redis_url, env.system_log))

            elif env.config.base.frequency == 'tick':
                from .tick_price_board import TickPriceBoard
                from .tick_pt_trading_validator import TickPTIsTradingValidator
                env.price_board = TickPriceBoard(redis_store)

                if env.config.base.run_type == RUN_TYPE.PAPER_TRADING:
                    from .tick_pt_event_source import TickPtEventSource
                    env.set_event_source(TickPtEventSource(mod_config.redis_url, env.system_log))
                    # 设置PT发单限制
                    env.add_frontend_validator(TickPTIsTradingValidator(env))

        #from deepquant.quest.datac import fenji
        #from deepquant.quest.api import register_api

        #register_api("fenji", fenji)

    def tear_down(self, success, exception=None):
        pass
