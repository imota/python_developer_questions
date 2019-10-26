#!/usr/bin/env python3

import pytest
from QuestionB import compareStrings

def test1():
    assert compareStrings('1.2', '1.1') == 1

def test2():
    assert compareStrings('1.2', '1.13') == -1

def test3():
    assert compareStrings('1.1', '1.2') == -1

def test4():
    assert compareStrings('1.13', '1.2') == 1

def test5():
    assert compareStrings('1.1', '1.1') == 0

def test6():
    assert compareStrings('1.13', '1.13') == 0

def test7():
    assert compareStrings('01.2', '1.1') == 1

def test8():
    assert compareStrings('01.2', '1.01') == 1

def test9():
    assert compareStrings('01', '002') == -1

def test10():
    assert compareStrings('002', '01') == 1

def test11():
    assert compareStrings('2.1', '2.02') == -1

def test12():
    assert compareStrings('2.1', '2') == 1

def test13():
    assert compareStrings('2.1 . 05 . 7', '2.1.05.7') == 0

def test14():
    assert compareStrings('02.1', '2.01') == 0