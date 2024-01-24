#!/usr/bin/env python3
'''store an instance of the Redis client'''
import uuid
import redis
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''count how many times methods of the Cache class are called'''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        output = f'{method.__qualname__}:outputs'
        input = f'{method.__qualname__}:inputs'
        self._redis.rpush(input, str(args))
        key = method(self, *args, **kwargs)
        output = self._redis.rpush(output, key)
        return key
    return wrapper

def replay(method: Callable) -> None:
    redis_instance = redis.Redis()
    input = f'{method.__qualname__}:inputs'
    output = f'{method.__qualname__}:outputs'
    input = redis_instance.lrange(input, 0, -1)
    output = redis_instance.lrange(output, 0, -1)
    for i, j in zip(output, input):
        j = j.decode("utf-8")
        i = i.decode("utf-8")
        print(f'{method.__qualname__}(*({j})) -> {i}')


class Cache:
    '''classs used to store item in database'''

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
