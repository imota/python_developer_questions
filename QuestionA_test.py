#!/usr/bin/env python3

from QuestionA import does_overlap
import unittest


class TestStringMethods(unittest.TestCase):

    def test_should_overlap_segment1_starts_to_the_left(self):
        self.assertTrue(does_overlap(1,5,2,6))

    def test_shouldnt_overlap_segment2_start_exactly_at_end_of_segment1(self):
        self.assertFalse(does_overlap(2,6,6,8))

    def test_should_overlap_segment1_starts_to_the_right(self):
        self.assertTrue(does_overlap(2,6,1,5))

    def test_shouldnt_overlap_segment2_ends_exactly_at_start_of_segment1(self):
        self.assertFalse(does_overlap(6,8,2,6))

    def test_should_overlap_equal_segments(self):
        self.assertTrue(does_overlap(6,8,6,8))

    def test_should_overlap_segment1_starts_to_the_left_negative_numbers(self):
        self.assertTrue(does_overlap(-10,-1,-5,0))

    def test_should_overlap_segment1_starts_to_the_right_negative_numbers(self):
        self.assertTrue(does_overlap(-5,0,-1,-10))

    def test_should_overlap_segment1_starts_to_the_left_inverted_segments(self):
        self.assertTrue(does_overlap(5,1,6,2))

    def test_should_overlap_segment2_inside_segment1(self):
        self.assertTrue(does_overlap(1,5,2,3))

    def test_should_overlap_segment1_inside_segment2(self):
        self.assertTrue(does_overlap(2,3,1,5))

    def test_should_overlap_segment1_starts_to_the_right_inverted_segments(self):
        self.assertTrue(does_overlap(2,3,1,5))

    def test_should_overlap_segment2_inside_segment1_negative_numbers(self):
        self.assertTrue(does_overlap(-1,-5,-2,-3))

    def test_should_overlap_segment1_inside_segment2_negative_numbers(self):
        self.assertTrue(does_overlap(-2,-3,-1,-5))

    def test_shouldnt_overlap_segment1_negative_segment2_positive(self):
        self.assertFalse(does_overlap(-1,-5,2,3))

    def test_shouldnt_overlap_segment1_positive_segment2_negative(self):
        self.assertFalse(does_overlap(-2,-3,1,5))

if __name__ == '__main__':
    unittest.main()