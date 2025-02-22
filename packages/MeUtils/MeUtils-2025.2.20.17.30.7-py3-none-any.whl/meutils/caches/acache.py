#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : acache
# @Time         : 2025/1/14 09:45
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :
import os

from meutils.pipe import *

from aiocache import cached

from aiocache import cached, Cache, RedisCache, caches
from aiocache import multi_cached



@cached(ttl=60)
@cached(ttl=60)
async def cached_fc(user_id, **kwargs):
    logger.debug(user_id)
    return False
#
rcache = RedisCache(
    endpoint="127.0.0.1", port=6379, namespace="me"  # 缓存键前缀
)
@cached(cache=rcache)
async def redis_fc(user_id, **kwargs):
    logger.debug(user_id)
    return False


# @multi_cached(ttl=60) # 多key缓存
# async def complex_function(user_id, **kwargs):
#     logger.debug(user_id)
#     return False


# Cache.MEMORY

# Cache.REDIS
# mcache = cached(ttl=60, cache=Cache.REDIS)(cached)
# from aiocache import Cache
#
# Cache(Cache.REDIS)
#
# rcache = Cache.from_url("redis://:chatfirechatfire@110.42.51.201:6379/11")
# print(rcache)


# @cached(ttl=60)
# @cached(ttl=15, cache=rcache)
# async def complex_function(user_id, **kwargs):
#     logger.debug(user_id)
#     return False
#

class A(BaseModel):
    a: Any = 1


if __name__ == '__main__':
    arun(cached_fc(A()))
