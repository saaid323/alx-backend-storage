#!/usr/bin/env python3
'''track how many times a particular URL was accessed '''
import redis
import requests
from typing import Callable


def track(method: Callable) -> Callable:
    '''function that track how many times a particular URL was accessed'''
    cache = redis.Redis()

    @wraps(method)
    def wrapper(url -> str) -> str:
        if cache.get(f'count:{url}'):
            cache.incr(f'count:{url}')
            return cache.get(f'count:{url}').decode("utf-8")
        cache.set(f'count:{url}', 1)
        cache.setex(f'result{url}', 10, method(url))
        return method(url)
    return wrapper


@track
def get_page(url: str) -> str:
    '''uses the requests module to obtain the HTML content of a particular
    URL and returns it.'''
    content = requests.get(url).text
    return content
