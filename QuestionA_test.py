#!/usr/bin/env python3

from QuestionA import does_overlap
import unittest


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertTrue(does_overlap(1,5,2,6))

    def test2(self):
        self.assertFalse(does_overlap(2,6,6,8))

    def test3(self):
        self.assertTrue(does_overlap(2,6,1,5))

    def test4(self):
        self.assertFalse(does_overlap(6,8,2,6))

    def test5(self):
        self.assertTrue(does_overlap(6,8,6,8))

    def test6(self):
        self.assertTrue(does_overlap(-10,-1,-5,0))

    def test7(self):
        self.assertTrue(does_overlap(-5,0,-1,-10))

    def test8(self):
        self.assertTrue(does_overlap(5,1,6,2))

    def test9(self):
        self.assertTrue(does_overlap(1,5,2,3))

    def test10(self):
        self.assertTrue(does_overlap(2,3,1,5))

    def test11(self):
        self.assertTrue(does_overlap(-1,-5,-2,-3))

    def test12(self):
        self.assertTrue(does_overlap(-2,-3,-1,-5))

    def test13(self):
        self.assertFalse(does_overlap(-1,-5,2,3))

    def test14(self):
        self.assertFalse(does_overlap(-2,-3,1,5))

if __name__ == '__main__':
    unittest.main()