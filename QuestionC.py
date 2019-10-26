#!/usr/bin/env python3

class LRUCache():
    def __init__(self, cache_capacity):
        self.cached_dictionary = {}
        self.cached_list = DoubleLinkedList()
        self.cache_count = 0
        self.cache_capacity = cache_capacity

    def get(self, key):
        if not key in self.cached_dictionary:
            return None
        item = self.cached_dictionary[key]
        self.cached_list.move_to_start(item)
        return item.value

    def put(self, key, value):
        pass

class DoubleLinkedList():
    def __init__(self):
        self.start = DoubleLinkedNode()
        self.end = DoubleLinkedNode(prev = self.start)
        self.start.next = self.end
        self.count = 0

    def move_to_start(self, node): #error trying to remove start or end
        self.remove(node)
        node.remove()
        self.add(node)
    
    def remove(self, node):
        node.remove()
        self.count -= 1

    def add(self, node):
        node.prev = self.start
        node.next = self.start.next
        self.start.next.prev = node
        self.start.next = node
        self.count += 1

    def pop(self):
        if self.end.prev != self.start:
            self.remove(self.end.prev)

class DoubleLinkedNode():
    def __init__(self, value = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev