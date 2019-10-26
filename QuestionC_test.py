#!/usr/bin/env python3

import pytest
from QuestionC import DoubleLinkedList
from QuestionC import DoubleLinkedNode
from QuestionC import LRUCache

def test_DoubleLinkedList_1():
    linked_list = DoubleLinkedList()
    linked_list.add_item(key = 1, item = 1)
    assert linked_list.count == 1

def test_DoubleLinkedList_2():
    linked_list = DoubleLinkedList()
    linked_list.add_item(key = 1, item = 5)
    assert linked_list.start.next.value == 5

def test_DoubleLinkedList_3():
    linked_list = DoubleLinkedList()
    linked_list.add_item(key = 1, item = 5)
    linked_list.pop()
    assert linked_list.count == 0

def test_DoubleLinkedList_4():
    linked_list = DoubleLinkedList()
    linked_list.add_item(key = 1, item = 5)
    linked_list.pop()
    assert linked_list.start.next == linked_list.end

def test_DoubleLinkedList_5():
    linked_list = DoubleLinkedList()
    linked_list.pop()
    assert linked_list.start.next == linked_list.end

def test_DoubleLinkedList_6():
    linked_list = DoubleLinkedList()
    linked_list.add_item(key = 1, item = 1)
    linked_list.add_item(key = 2, item = 3)
    assert linked_list.count == 2

def test_DoubleLinkedList_7():
    linked_list = DoubleLinkedList()
    linked_list.add_item(key = 1, item = 1)
    linked_list.add_item(key = 2, item = 3)
    assert linked_list.start.next.next.value == 1

def test_DoubleLinkedList_8():
    linked_list = DoubleLinkedList()
    linked_list.add_item(key = 1, item = 1)
    linked_list.add_item(key = 2, item = 3)
    assert linked_list.end.prev.prev.value == 3

def test_DoubleLinkedList_9():
    linked_list = DoubleLinkedList()
    linked_list.add_item(key = 1, item = 1)
    linked_list.add_item(key = 1, item = 3)
    assert linked_list.count == 2

def test_LRUCache_1():
    cache = LRUCache(cache_capacity = 1)
    cache.put(1, 5)
    assert cache.get(1) == 5

def test_LRUCache_2():
    cache = LRUCache(cache_capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    assert cache.get(1) == None

def test_LRUCache_3():
    cache = LRUCache(cache_capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    assert cache.get(2) == 3

def test_LRUCache_4():
    cache = LRUCache(cache_capacity = 1)
    cache.put(1, 5)
    cache.put(1, 3)
    assert cache.get(1) == 3

def test_LRUCache_5():
    cache = LRUCache(cache_capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    assert cache.get_cache_count() == 1

def test_LRUCache_6():
    cache = LRUCache(cache_capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    assert cache.get(2) == 3

def test_LRUCache_7():
    cache = LRUCache(cache_capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    cache.delete(2)
    assert cache.cache_count == 0

def test_LRUCache_8():
    cache = LRUCache(cache_capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    cache.delete(2)
    assert cache.get(2) == None

def test_LRUCache_9():
    cache = LRUCache(cache_capacity = 1)
    cache.put(1, 5)
    cache.put(2, 3)
    cache.delete(1)
    assert cache.cache_count == 1