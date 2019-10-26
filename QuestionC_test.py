#!/usr/bin/env python3

import pytest
from QuestionC import DoubleLinkedList
from QuestionC import DoubleLinkedNode

def test1():
    linked_list = DoubleLinkedList()
    linked_list.add(DoubleLinkedNode(value = 1))
    assert linked_list.count == 1

def test2():
    linked_list = DoubleLinkedList()
    linked_list.add(DoubleLinkedNode(value = 5))
    assert linked_list.start.next.value == 5

def test3():
    linked_list = DoubleLinkedList()
    linked_list.add(DoubleLinkedNode(value = 5))
    linked_list.pop()
    assert linked_list.count == 0

def test4():
    linked_list = DoubleLinkedList()
    linked_list.add(DoubleLinkedNode(value = 5))
    linked_list.pop()
    assert linked_list.start.next == linked_list.end

def test5():
    linked_list = DoubleLinkedList()
    linked_list.pop()
    assert linked_list.start.next == linked_list.end

def test6():
    linked_list = DoubleLinkedList()
    linked_list.add(DoubleLinkedNode(value = 1))
    linked_list.add(DoubleLinkedNode(value = 3))
    assert linked_list.count == 2

def test7():
    linked_list = DoubleLinkedList()
    linked_list.add(DoubleLinkedNode(value = 1))
    linked_list.add(DoubleLinkedNode(value = 3))
    assert linked_list.start.next.next.value == 1

def test8():
    linked_list = DoubleLinkedList()
    linked_list.add(DoubleLinkedNode(value = 1))
    linked_list.add(DoubleLinkedNode(value = 3))
    assert linked_list.end.prev.prev.value == 3