# -*- coding: utf-8 -*-
#
# Copyright 2016 Ricequant, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import simplejson as json
import redis


class Redis(redis.client.Redis):
    def execute_command(self, *args, **options):
        pool = self.connection_pool
        command_name = args[0]
        connection = pool.get_connection(command_name, **options)
        try:
            connection.send_command(*args)
            return self.parse_response(connection, command_name, **options)
        except (ConnectionError, TimeoutError, redis.exceptions.RedisError) as e:
            connection.disconnect()
            connection.send_command(*args)
            return self.parse_response(connection, command_name, **options)
        finally:
            pool.release(connection)


class RedisStore:
    snapshot_prefix = "snapshot:"
    tick_prefix = "tick_"
    # bar_prefix = "bar:"

    def __init__(self, redis_url):
        self._redis = Redis.from_url(redis_url)

    def get_current_bar(self, market_code):
        v = self._redis.lindex(market_code, -1)
        if v is None:
            return None
        bar = json.loads(v.decode())
        return bar

    def get_settle_price(self, market_code):
        v = self._redis.hget('settlement', market_code)
        if v is None:
            return np.nan
        return float(v)

    def history(self, market_code, bar_count):
        values = self._redis.lrange(market_code, -bar_count, -1)
        if values is None:
            return []

        return [json.loads(v.decode()) for v in values]

    def get_snapshot(self, market_code):
        v = self._redis.get(RedisStore.snapshot_prefix + market_code)
        if v is None:
            return None
        snapshot = json.loads(v.decode())

        if "asks" not in snapshot:
            snapshot["asks"] = snapshot.get("ask", [])
        if "bids" not in snapshot:
            snapshot["bids"] = snapshot.get("bid", [])
        if "ask_vols" not in snapshot:
            snapshot["ask_vols"] = snapshot.get("ask_vol", [])
        if "bid_vols" not in snapshot:
            snapshot["bid_vols"] = snapshot.get("bid_vol", [])

        # snapshot["datetime"] //= 1000
        return snapshot

    def history_ticks(self, market_code, count):
        key = self.tick_prefix + market_code
        values = self._redis.lrange(key, -count, -1)
        if values is None:
            return []

        return [json.loads(v.decode()) for v in values]