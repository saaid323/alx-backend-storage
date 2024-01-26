#!/usr/bin/env python3
'''track how many times a particular URL was accessed '''
import redis
import requests
from typing import Callable


def track(method: Callable) -> Callable:
    '''function that track how many times a particular URL was accessed'''
    cache = redis.Redis()

    @wraps(method)
    def wrapper(url):
        if cache.exists(f'count:{url}'):
            cache.incr(f'count:{url}')
            cache.setex(f'count:{url}', 10, cache.get(f'count:{url}'))
        else:
            cache.setex(f'count:{url}', 10, 1)
        return method(url)
    return wrapper


@track
def get_page(url: str) -> str:
    '''uses the requests module to obtain the HTML content of a particular
    URL and returns it.'''
    content = requests.get(url).text
    return content
