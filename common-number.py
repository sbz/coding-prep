#!/usr/bin/env python

"""
Problem:
   Given 2 arrays sorted and distinct, find the common numbers in the
   both arrays

   [1,12,15,19,20,21] and [2,15,17,19,21,25] -> [15,19,21]
"""

from binary_search import binary_search

def find_common_number(array1, array2):
    """
    Time O(n*n)
    Space O(n)
    """
    result = []

    for i in range(0, len(array1)):
        for j in range(0, len(array2)):
            if array1[i] == array2[j]:
                result.append(array1[i])

    return result

def find_common_number_linear(array1, array2):
    """
    Time O(n*log(n))
    Space O(n)
    """
    result = []
    for number in array1:
        index = binary_search(array2, number)
        if array2[index] == number:
            result.append(number)

    return result

# Test

import unittest

class Test(unittest.TestCase):

    def test_find_common_number(self):
        array1 = [1,12,15,19,20,21]
        array2 = [2,15,17,19,21,25]
        expected = [15,19,21]
        result = find_common_number(array1, array2)
        self.assertEqual(result, expected)

    def test_find_common_number_linear(self):
        array1 = [1,12,15,19,20,21]
        array2 = [2,15,17,19,21,25]
        expected = [15,19,21]
        result = find_common_number_linear(array1, array2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
