#!/usr/bin/env python3
'''store an instance of the Redis client'''
import uuid
import redis
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable):
    '''count how many times methods of the Cache class are called''' 
    name = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(name, amount=1)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    '''classs used to store item in database'''

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return str(key)

    def get(self,
            key: str,
            fn: Callable = None) -> Union[str,
                                          bytes,
                                          int,
                                          float,
                                          None]:
        if self._redis.exists(key) == False:
            return None
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        return self.get(key, int)


# cache = Cache()

# TEST_CASES = {
    #b"foo": None,
    # 123: int,
    # "bar": lambda d: d.decode("utf-8")
# }

# for value, fn in TEST_CASES.items():
    # key = cache.store(value)
    # assert cache.get(key, fn=fn) == value
