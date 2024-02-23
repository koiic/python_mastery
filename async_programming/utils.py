import time
from typing import Callable


def async_timed(func: Callable):
    async def wrappper(*args, **kwargs):
        start = time.time()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.time()
            total = end - start
            print(f'finished {func} in {total:.4f} second(s)')

    return wrappper
