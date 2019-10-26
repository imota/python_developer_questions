#!/usr/bin/env python3

import pytest
from QuestionC import LRUCache
from QuestionC import Item

def test_LRUCache_1():
    cache = LRUCache(capacity = 1)
    cache.put(1, 5)
    assert cache.get(1) == 5

def test_LRUCache_2():
    cache = LRUCache(capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    assert cache.get(1) == None

def test_LRUCache_3():
    cache = LRUCache(capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    assert cache.get(2) == 3

def test_LRUCache_4():
    cache = LRUCache(capacity = 1)
    cache.put(1, 5)
    cache.put(1, 3)
    assert cache.get(1) == 3

def test_LRUCache_5():
    cache = LRUCache(capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    assert cache.get_cache_count() == 1

def test_LRUCache_6():
    cache = LRUCache(capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    assert cache.get(2) == 3

def test_LRUCache_7():
    cache = LRUCache(capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    cache.delete(2)
    assert cache.get_cache_count() == 0

def test_LRUCache_8():
    cache = LRUCache(capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    cache.delete(2)
    assert cache.get(2) == None

def test_LRUCache_9():
    cache = LRUCache(capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    cache.delete(1)
    assert cache.get_cache_count() == 1