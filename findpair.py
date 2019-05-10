#!/usr/bin/env python

import itertools

"""
Problem:
    Find the pairs (x, y) of numbers in the array which sum to S

    Input -> Output

    [1, 5, -3, 2, 10, 8, -1]  and S = 7 -> [(-3, 10), (5, 2), (8, -1)]
"""

def find_pairs_sum(array, s):
    """
    Time O(n*n)
    Space O(n)
    """
    result = []

    if array is None:
        return result

    for i in range(0, len(array)):
        for j in range(i, len(array)):
            x = array[i]
            y = array[j]
            if x + y == s:
                result.append((x, y))

    return result

def find_pairs_sum_itertools(array, s):
    """
    Better according runtime of itertools.combinations()

    Time O(itertools.combinations()) -> O(n)
    Space O(n)
    """
    result = []

    if array is None:
        return result

    for pair in itertools.combinations(array, 2):
        x = pair[0]
        y = pair[1]
        if x + y == s:
            result.append((x, y))

    return result

# Test

import unittest

class Test(unittest.TestCase):

    def test_find_pairs(self):
        array = [1, 5, -3, 2, 10, 8, -1]
        s = 7
        expected = [(-3, 10), (5, 2), (8, -1)]
        result = find_pairs_sum_itertools(array, s)
        result.sort() # sort to have same order as expected
        self.assertEqual(result, expected)

    def test_find_pairs_only_positive_number(self):
        array = [1, 5, 3, 2, 10, 6, 4]
        s = 7
        expected = [(1, 6), (3, 4), (5, 2)]
        result = find_pairs_sum_itertools(array, s)
        result.sort() # sort to have same order as expected
        self.assertEqual(result, expected)

    def test_find_pairs_only_negative_number(self):
        array = [-1, -5, -3, -2, -10, -6, -4]
        s = 7
        expected = []
        result = find_pairs_sum_itertools(array, s)
        self.assertEqual(result, expected)

    def test_find_pairs_no_exisiting_sum(self):
        array = [1, 5, 10, 4]
        s = 7
        expected = []
        result = find_pairs_sum_itertools(array, s)
        self.assertEqual(result, expected)

    def test_find_pairs_negative_sum(self):
        array = [1, 5, -10, 4, 3]
        s = -7
        expected = [(-10, 3)]
        result = find_pairs_sum_itertools(array, s)
        self.assertEqual(result, expected)

    def test_find_pairs_empty_array(self):
        array = []
        s = 7
        expected = []
        result = find_pairs_sum_itertools(array, s)
        self.assertEqual(result, expected)

    def test_find_pairs_none_array(self):
        array = None
        s = 7
        expected = []
        result = find_pairs_sum_itertools(array, s)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
