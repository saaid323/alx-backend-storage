#!/usr/bin/env python3
""" Main file """
from exercise import Cache, replay
cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
