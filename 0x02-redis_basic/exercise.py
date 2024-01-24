#!/usr/bin/env python3
'''store an instance of the Redis client'''
import uuid
import redis
from typing import Unioin, Callable


class Cache:
    '''classs used to store item in database'''

    def __init__(self):
        self._redis = redis.Redis()
        self.flush = self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = uuid.uuid4()
        store = self._redis.set(str(key), data)
        self.flush
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
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)
