#!/usr/bin/python

"""
Problem: 
    Design and implement a data structure for Least Recently Used (LRU) cache.
    It should support the following operations: get(key) and put(key, value).

References:
    https://leetcode.com/problems/lru-cache/
"""

from collections import OrderedDict

class LRUCache(object):
    """
    collections.OrdereDict help to keep the insertion order in the cache.

    Time O(1)
    Space O(n)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        if self.capacity < 0:
            raise Exception("Cache capacity must be > 0")
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)

        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def __str__(self):
        return str(self.cache)

# Test

import unittest

class LRUCacheTest(unittest.TestCase):

    def test_key_evicted(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), -1)

    def test_key_cached(self):
        cache = LRUCache(1)
        cache.put(1, 42)
        self.assertEqual(cache.get(1), 42)

    def test_key_updated(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 42)
        self.assertEqual(cache.get(1), 42)

    def test_key_not_cached(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(42), -1)

    def test_cache_negative_capacity(self):
        with self.assertRaises(Exception):
            cache = LRUCache(-2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
