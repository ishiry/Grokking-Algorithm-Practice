import unittest
import logging.handlers


from grokking_algorithm_practice.practice.chapter1.binarySearch import binary_search

class TestBinarySearch(unittest.TestCase):
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_binary_search_mid(self):
        result = binary_search(self.my_list, 5)
        expected = 4
        self.assertEqual(result, expected)

    def test_binary_search_none(self):
        result = binary_search(self.my_list, 10)
        expected = None
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
