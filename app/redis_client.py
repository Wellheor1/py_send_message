import json
import logging
import os
from functools import wraps
from typing import Callable

import redis as redis_app

from redis import Redis

from app.settings import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD

redis = None
logger = logging.getLogger("uvicorn.error")


def create_redis_url():
    if REDIS_PASSWORD:
        redis_url = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    else:
        redis_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    return redis_url


def init_redis():
    global redis
    # redis_url = create_redis_url()
    # redis = redis_app.from_url(redis_url, decode_responses=True)
    redis = redis_app.Redis(
        host=os.getenv("REDIS_HOST", REDIS_HOST),
        port=int(os.getenv("REDIS_PORT", REDIS_PORT)),
        password=(os.getenv("REDIS_PASSWORD", REDIS_PASSWORD)),
        db=int(os.getenv("REDIS_DB", REDIS_DB)),
    )
    redis_ping = redis.ping()
    if redis_ping:
        logger.info("Redis connected")
    else:
        logger.error("Redis not connected")


def close_redis():
    global redis
    if redis:
        redis.close()
        logger.info("Redis disconnected")


def get_redis() -> Redis:
    return redis


def cache(expire: int = 60):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                async with get_redis() as r:
                    cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
                    cached_result = r.get(cache_key)
                    if cached_result:
                        return json.loads(cached_result)
                    result = await func(*args, **kwargs)
                    r.setex(cache_key, expire, json.dumps(result))
                    return result
            except Exception as e:
                logger.error(f"Redis cache error: {e}")
                return await func(*args, **kwargs)

        return wrapper

    return decorator
