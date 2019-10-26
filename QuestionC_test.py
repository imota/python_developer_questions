#!/usr/bin/env python3

from datetime import timedelta, datetime
from QuestionC import LRUCache, Item
import unittest
import time

class TestStringMethods(unittest.TestCase):

    def test_LRUCache_1(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        self.assertEqual(cache.get(1), 5)

    def test_LRUCache_2(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        self.assertEqual(cache.get(1), None)

    def test_LRUCache_3(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        self.assertEqual(cache.get(2), 3)

    def test_LRUCache_4(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(1, 3)
        self.assertEqual(cache.get(1), 3)

    def test_LRUCache_5(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        self.assertEqual(cache.get_cache_count(), 1)

    def test_LRUCache_6(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        self.assertEqual(cache.get(2), 3)

    def test_LRUCache_7(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        cache.delete(2)
        self.assertEqual(cache.get_cache_count(), 0)

    def test_LRUCache_8(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        cache.delete(2)
        self.assertEqual(cache.get(2), None)

    def test_LRUCache_9(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        cache.delete(1)
        self.assertEqual(cache.get_cache_count(), 1)

    def test_LRUCache_10(self):
        cache = LRUCache(capacity = 1, expiration_time = timedelta(milliseconds=1))
        cache.put(1, 5)
        time.sleep(0.1)
        self.assertEqual(cache.get(1), None)

if __name__ == '__main__':
    unittest.main()