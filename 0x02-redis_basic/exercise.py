#!/usr/bin/env python3
'''store an instance of the Redis client'''
import uuid
import redis
from typing import Union


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

    def get(self, key: str, fn: Callable=None) -> Union[str, bytes, int, float]:
        if fn is not None:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, data: str) -> str:
        return self.get(data, lambda d: d.decode("utf-8"))

    def get_int(self, data: str) -> int:
        return self.get(data, lambda d: int(d))
