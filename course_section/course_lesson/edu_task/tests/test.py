import unittest
from main import sum_two_numbers


class TestCase(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(367, sum_two_numbers(100, 267), msg="Wrong result for numbers 100 and 267")

    def test_negative_numbers(self):
        self.assertEqual(-367, sum_two_numbers(-100, -267), msg="Wrong result for numbers -100 and -267")
