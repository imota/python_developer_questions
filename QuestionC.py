#!/usr/bin/env python3

'''
TODO:
1 - Time expiration
2 - Resilient to network failures or crashes.
3 - Near real time replication of data across Geolocation. Writes need to be in real time.
4 - Data consistency across regions
5 - Locality of reference, data should almost always be available from the closest region
6 - Flexible Schema
'''
class LRUCache():
    def __init__(self, cache_capacity):
        self.cached_dictionary = {}
        self.cached_list = DoubleLinkedList()
        self.cache_count = 0
        self.cache_capacity = cache_capacity

    def _free_cache(self):
        removed_item = self.cached_list.pop()
        if removed_item != None:
            self.cached_dictionary.pop(removed_item.key, None)
            self.cache_count -= 1

    def get_free_capacity(self):
        return self.cache_capacity - self.cache_count

    def get_cache_count(self):
        return self.cache_count

    def get(self, key):
        if not key in self.cached_dictionary:
            return None
        item = self.cached_dictionary[key]
        self.cached_list.move_to_start(item)
        return item.value

    def put(self, key, value):
        if key in self.cached_dictionary:
            item = self.cached_dictionary[key]
            item.value = value
            self.cached_list.move_to_start(item)
        else:
            if self.cache_count == self.cache_capacity:
                self._free_cache()
            new_item = self.cached_list.add_item(key, value)
            self.cached_dictionary[key] = new_item
            self.cache_count += 1

class DoubleLinkedList():
    def __init__(self):
        self.start = DoubleLinkedNode()
        self.end = DoubleLinkedNode(prev = self.start)
        self.start.next = self.end
        self.count = 0

    def move_to_start(self, node): #error trying to remove start or end
        self.remove(node)
        node.remove()
        self._add_node(node)
    
    def remove(self, node):
        node.remove()
        self.count -= 1

    def add_item(self, key, item):
        new_node = DoubleLinkedNode(key = key, value = item)
        self._add_node(new_node)
        return new_node

    def _add_node(self, node):
        node.prev = self.start
        node.next = self.start.next
        self.start.next.prev = node
        self.start.next = node
        self.count += 1

    def pop(self):
        item = self.end.prev
        if item != self.start:
            self.remove(item)
            return item
        return None

class DoubleLinkedNode():
    def __init__(self, key = None, value = None, prev = None, next = None):
        self.key = key #we store the key to make deletion from the dictionary based on the node faster
        self.value = value
        self.prev = prev
        self.next = next

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev