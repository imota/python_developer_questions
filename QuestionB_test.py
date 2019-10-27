#!/usr/bin/env python3

from QuestionB import compare_version_strings
import unittest

class TestQuestionB(unittest.TestCase):

    def test1(self):
        self.assertEqual(compare_version_strings('1.2', '1.1'), 1)

    def test2(self):
        self.assertEqual(compare_version_strings('1.2', '1.13'), -1)

    def test3(self):
        self.assertEqual(compare_version_strings('1.1', '1.2'), -1)

    def test4(self):
        self.assertEqual(compare_version_strings('1.13', '1.2'), 1)

    def test5(self):
        self.assertEqual(compare_version_strings('1.1', '1.1'), 0)

    def test6(self):
        self.assertEqual(compare_version_strings('1.13', '1.13'), 0)

    def test7(self):
        self.assertEqual(compare_version_strings('01.2', '1.1'), 1)

    def test8(self):
        self.assertEqual(compare_version_strings('01.2', '1.01'), 1)

    def test9(self):
        self.assertEqual(compare_version_strings('01', '002'), -1)

    def test10(self):
        self.assertEqual(compare_version_strings('002', '01'), 1)

    def test11(self):
        self.assertEqual(compare_version_strings('2.1', '2.02'), -1)

    def test12(self):
        self.assertEqual(compare_version_strings('2.1', '2'), 1)

    def test_should_be_equal_same_number_with_spaces(self):
        self.assertEqual(compare_version_strings('2.1 . 05 . 7', '2.1.05.7'), 0)

    def test_should_be_equal_same_number_with_zeros_to_the_left(self):
        self.assertEqual(compare_version_strings('02.1', '2.01'), 0)

if __name__ == '__main__':
    unittest.main()