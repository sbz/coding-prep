#!/usr/bin/env python

"""
Problem:
    Find the n largest element in the array

[3,4,5,10,12] -> n = 1, 12
              -> n = 3, 5
              -> n = 5, 3

References:
    https://en.wikipedia.org/wiki/Selection_algorithm
    https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
"""

def find_largest(array, n):
    """
    Time O(n*log(n))
    Space O(1)
    """
    if n < 0:
        return None

    size = len(array)
    if size == 0 or n > size:
        return None

    array.sort()

    return array[size - n]

def find_largest_linear(array, n):
    """
    Time O(n)
    Space O(n)
    """
    size = len(array)
    if size == 0 or n > size:
        return None

    maxs = []
    current = array[0]

    for number in array[1:]:
        if n > 0 and number > current:
            maxs.append(number)
            current = number

    return maxs[n]

import heapq

def find_largest_heap(array, k):
    """
    Time O(k*log(n))
    Space O(n+k*log(n))
    """
    size = len(array)
    if size == 0 or k > size or k < 0:
        return None

    return heapq.nlargest(k, array)[-1]

import unittest

class Test(unittest.TestCase):

    def test_largest_1(self):
        n = 2
        array = [3,4,5,10,12]
        result = find_largest_heap(array, n)
        excepted = 10
        self.assertEqual(result, excepted)

    def test_largest_2(self):
        n = 1
        array = [3,4,5,10,12]
        result = find_largest_heap(array, n)
        excepted = 12
        self.assertEqual(result, excepted)

    def test_largest_3(self):
        n = 2
        array = [-1,-4,-5,-10,-12]
        result = find_largest_heap(array, n)
        excepted = -4
        self.assertEqual(result, excepted)

    def test_largest_empty_array(self):
        n = 2
        array = []
        result = find_largest_heap(array, n)
        excepted = None
        self.assertIsNone(None)

    def test_largest_n_positive_outofbounds(self):
        array = [-1,-4,-5,-10,-12]
        n = len(array) + 1
        result = find_largest_heap(array, n)
        excepted = None
        self.assertIsNone(None)

    def test_largest_n_negative_outofbounds(self):
        array = [-1,-4,-5,-10,-12]
        n = -len(array) -1
        result = find_largest_heap(array, n)
        excepted = None
        self.assertIsNone(None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
