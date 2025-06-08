import aioredis
from contextlib import asynccontextmanager

redis = None


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
