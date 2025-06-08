import json
import logging
from functools import wraps
from typing import Callable

import aioredis
from contextlib import asynccontextmanager

redis = None
logger = logging.getLogger("uvicorn.error")


async def init_redis():
    global redis
    redis = await aioredis.from_url("redis://127.0.0.1:6379/2", decode_responses=True)


async def close_redis():
    global redis
    if redis:
        await redis.close()


@asynccontextmanager
async def get_redis():
    yield redis


def cache(expire: int = 60):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                async with get_redis() as r:
                    # Формируем уникальный ключ для кэша
                    cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
                    # Проверяем, есть ли данные в кэше
                    cached_result = await r.get(cache_key)
                    if cached_result:
                        return json.loads(cached_result)
                    result = await func(*args, **kwargs)
                    await r.setex(cache_key, expire, json.dumps(result))
                    return result
            except Exception as e:
                logger.error(f"Redis cache error: {e}")
                return await func(*args, **kwargs)

        return wrapper

    return decorator
