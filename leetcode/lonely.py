#!/usr/bin/env python

"""
Problem:
    Find the single integer in the given array

    Input -> Output
    [] -> None
    [-7, 3, -7] -> 3
    [7, -3, 7] -> -3
    [5, 5] -> None
    [4] -> 4

Reference:
    https://leetcode.com/problems/single-element-in-a-sorted-array/
"""

import collections

def lonely(array):
    """
    Time O(n)
    Space O(n)
    """
    if len(array) == 0:
        return None

    if len(array) == 1:
        return array[0]

    count = collections.defaultdict(int)

    for num in array:
        count[num] += 1

    single = [int(num) for num in count if count[num] == 1]
    if len(single) == 0:
        return None

    return single[0]

def lonely_space(array):
    """
    The trick is to use XOR operator to find the unique element

    Time O(n)
    Space O(1)
    """
    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]

    result = array[0]
    for num in array[1:]:
        result ^= num

    if result == 0:
        return None

    return result
 
# Test

import unittest

class Test(unittest.TestCase):

    def test_lonely_ko(self):
        self.assertEqual(None, lonely([]))
        self.assertEqual(None, lonely([5, 5]))
        self.assertEqual(None, lonely_space([]))
        self.assertEqual(None, lonely_space([5, 5]))

    def test_lonely_ok(self):
        self.assertEqual(14, lonely([2, 2, 3, 4, 4, 14, 3, 5, 7, 5, 7]))
        self.assertEqual(14, lonely_space([2, 2, 3, 4, 4, 14, 3, 5, 7, 5, 7]))
        self.assertEqual(3, lonely([-7, 3, -7]))
        self.assertEqual(3, lonely_space([-7, 3, -7]))
        self.assertEqual(-3, lonely([7, -3, 7]))
        self.assertEqual(-3, lonely_space([7, -3, 7]))
        self.assertEqual(4, lonely([4]))
        self.assertEqual(4, lonely_space([4]))

if __name__ == '__main__':
    unittest.main(verbosity=2)
