#!/usr/bin/env python3

import pytest
from QuestionA import doesOverlap

def test1():
    assert doesOverlap(1,5,2,6) == True

def test2():
    assert doesOverlap(2,6,6,8) == False

def test3():
    assert doesOverlap(2,6,1,5) == True

def test4():
    assert doesOverlap(6,8,2,6) == False

def test5():
    assert doesOverlap(6,8,6,8) == True

def test6():
    assert doesOverlap(-10,-1,-5,0) == True

def test7():
    assert doesOverlap(-5,0,-1,-10) == True

def test8():
    assert doesOverlap(5,1,6,2) == True

def test9():
    assert doesOverlap(1,5,2,3) == True

def test10():
    assert doesOverlap(2,3,1,5) == True

def test11():
    assert doesOverlap(-1,-5,-2,-3) == True

def test12():
    assert doesOverlap(-2,-3,-1,-5) == True

def test13():
    assert doesOverlap(-1,-5,2,3) == False

def test14():
    assert doesOverlap(-2,-3,1,5) == False