import logging

logger = logging.getLogger(__name__)


def say_hello(name):
    if not isinstance(name, str):
        logger.error("`name` is not a string, not saying hello")
        return
    print(f"Hello, {name}")
