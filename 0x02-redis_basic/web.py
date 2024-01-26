#!/usr/bin/env python3
'''track how many times a particular URL was accessed '''
import redis
import requests
from typing import Callable


def track(method: Callable) -> Callable:
    cache = redis.Redis()
    @wraps(method)
    def wrapper(url) -> str:
        if cache.exists(content):
            value = cache.
            cache.incr('count:{url}')
            cache.setex('')


def get_page(url: str) -> str:
    '''function that track how many times a particular URL was accessed '''
    content = requests.get(url).text
    cache = redis.Redis()
    if cache.exists(content):
        cache.incr(f'count:{url}')
    else:
        cache.setex('url', 10, 1)
