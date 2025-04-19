import functools
import logging


def logged(function):
    @functools.wraps(function)
    async def wrapper(*args, **kwargs):
        logging.info("до функции")
        result = await function(*args, **kwargs)
        logging.info("после функции")
        return result

    return wrapper
