import os
import sys
import unittest
from io import StringIO


dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f"{dir_path}/../src")

from algorithm import SimpleSearch


class TestStringMethods(unittest.TestCase):
    """
        Test three cases for algorithm.
        1. when string is not found in offerd file
        2. when string is found in offer file
        3. when overlap occurs
    """

    def test_not_find(self):
        self.assertEqual(SimpleSearch(StringIO("hey I am a test")).search("haha")["number_of_occurrences"], 0)

    def test_find(self):
        document = SimpleSearch(StringIO("Hills looks far away. We love them."))

        self.assertEqual(document.search("Hills")["number_of_occurrences"], 1)
        self.assertEqual(document.search("Hills")["occurrences"][0]["in_sentence"], "Hills looks far away.")

    def test_overlap(self):
        self.assertEqual(SimpleSearch(StringIO("hahaha")).search("haha")["number_of_occurrences"], 2)


if __name__ == '__main__':
    unittest.main()
