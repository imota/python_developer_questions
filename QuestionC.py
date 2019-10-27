#!/usr/bin/env python3

from datetime import datetime, timedelta
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity, expiration_time = timedelta.max):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.expiration_time = expiration_time

    def has_expired(self, item):
        return self.expiration_time < datetime.now() - item.last_update

    def get_free_capacity(self):
        return self.capacity - len(self.cache)

    def get_cache_count(self):
        return len(self.cache)

    def delete(self, key):
        self.cache.pop(key, None)

    def get(self, key):
        item = self.cache.pop(key, None)
        if item == None or self.has_expired(item):
            raise TypeError

        if item != None:
            self.cache[key] = item
        return item.value

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key, None)
        elif not self.has_free_space():
            self.cache.popitem()
        self.cache[key] = Item(value = value)   

    def has_free_space(self):
        return len(self.cache) < self.capacity

    def move_to_start(self, item):
        self.delete(item.key)
        self.cache[item.key] = item

class Item:
    def __init__(self, value = None):
        self.value = value
        self.last_update = datetime.now()