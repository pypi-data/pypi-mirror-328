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
cimport numpy as np
cimport cython


@cython.cdivision(True)
cdef inline np.int64_t _to_minute(np.uint64_t dt):
    cdef np.int64_t hour, minute
    dt = dt % 1000000
    hour = dt / 10000
    minute = (dt % 10000) / 100
    return hour * 60 + minute


@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
@cython.nonecheck(False)
def to_minutes(np.ndarray[np.uint64_t, ndim=1] dt_array):
    cdef np.int64_t x, start
    cdef np.int64_t hour, minute
    cdef np.int64_t array_len = len(dt_array)

    cdef np.ndarray[np.int64_t, ndim=1] result = np.empty(array_len, np.int64)
    start = _to_minute(dt_array[0])

    for pos in range(len(dt_array)):
        x = _to_minute(dt_array[pos]) - start
        if x < 0:
            x += 24*60
        result[pos] = x

    return result


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
def unique_sorted(np.ndarray[np.int64_t, ndim=1] array):
    cdef np.int64_t pos = 0
    cdef np.int64_t array_len = len(array)
    cdef size_t x

    result = []
    for x in range(array_len - 1):
        if array[x] != array[x+1]:
            result.append(array[x])
    result.append(array[array_len - 1])

    return np.array(result)

