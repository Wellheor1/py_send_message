import functools
import logging

logger = logging.getLogger("uvicorn.error")


def logged(function):
    @functools.wraps(function)
    async def wrapper(*args, **kwargs):
        logger.info("до функции")
        result = await function(*args, **kwargs)
        logger.info("после функции")
        return result

    return wrapper
