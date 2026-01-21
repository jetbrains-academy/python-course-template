import unittest
from main import multiply_two_numbers


class TestCase(unittest.TestCase):

    def test_multiply_numbers(self):
        self.assertEqual(132, multiply_two_numbers(11 ,12), msg="Wrong result for numbers 11 and 12")
