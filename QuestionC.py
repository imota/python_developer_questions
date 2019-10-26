#!/usr/bin/env python3

from datetime import datetime
from datetime import timedelta
from collections import OrderedDict

'''
TODO:
1 - Time expiration
2 - Resilient to network failures or crashes.
3 - Near real time replication of data across Geolocation. Writes need to be in real time.
4 - Data consistency across regions
5 - Locality of reference, data should almost always be available from the closest region
6 - Flexible Schema
'''
class LRUCache:
    def __init__(self, capacity, expiration_time = timedelta.max):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.expiration_time = expiration_time

    def has_expired(self, key):
        return False

    def get_free_capacity(self):
        return self.capacity - len(self.cache)

    def get_cache_count(self):
        return len(self.cache)

    def delete(self, key):
        self.cache.pop(key, None)

    def get(self, key):
        item = self.cache.pop(key, None)
        if item == None or self.expiration_time < datetime.now() - item.last_update:
            return None

        if item != None:
            self.cache[key] = item
        return item.value

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key, None)
        elif not self.has_free_space():
            del self.cache[list(self.cache.keys())[-1]]
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

    def update(self, value):
        self.value = value
        self.last_update = datetime.now()
        return self