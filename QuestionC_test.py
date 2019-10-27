#!/usr/bin/env python3

from datetime import timedelta, datetime
from QuestionC import LRUCache, Item
import time
import unittest

class TestStringMethods(unittest.TestCase):

    def test_LRUCache_put_1(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        self.assertEqual(cache.get(1), 5)

    def test_LRUCache_put_2_capacity_1_shouldnt_find_first(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        self.assertEqual(cache.get(1), None)

    def test_LRUCache_put_2_capacity_1_find_second(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        self.assertEqual(cache.get(2), 3)

    def test_LRUCache_put_2_same_key(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(1, 3)
        self.assertEqual(cache.get(1), 3)

    def test_LRUCache_put_2_capacity_1_cached_count_should_be_1(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        self.assertEqual(cache.get_cache_count(), 1)

    def test_LRUCache_put_2_capacity_1_delete_1_count_should_be_0(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        cache.delete(2)
        self.assertEqual(cache.get_cache_count(), 0)

    def test_LRUCache_put_2_capacity_1_delete_1_get_shouldnt_find_anything(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        cache.delete(2)
        self.assertEqual(cache.get(2), None)

    def test_LRUCache_delete_already_removed_element(self):
        cache = LRUCache(capacity = 1)
        cache.put(1, 5)
        cache.put(2, 3)
        cache.delete(1)
        self.assertEqual(cache.get_cache_count(), 1)

    def test_LRUCache_get_after_time_expiration_shouldnt_find(self):
        cache = LRUCache(capacity = 1, expiration_time = timedelta(milliseconds=1))
        cache.put(1, 5)
        time.sleep(0.1)
        self.assertEqual(cache.get(1), None)

if __name__ == '__main__':
    unittest.main()