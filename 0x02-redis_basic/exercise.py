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
