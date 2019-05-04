#!/usr/bin/env python

"""
Problem:
    Find if there is any dupplicate in array of the size N
"""
# Are Numbers all Integer?
# Does it need to return all the number or just a boolean?
# Does it need to return if we detect one?
# What is the output format?

def hasDupplicate(array):
    """
    Time O(n)
    Space O(n)
    """
    count = {}
    has_dup = False

    if len(array) < 2:
        return has_dup, []

    for n in array:
        if n not in count:
            count[n] = 1
        else:
            count[n] = 1 + count[n]
            has_dup = True

    return has_dup, [n for n in count if count[n] > 1]

import unittest

class Test(unittest.TestCase):

    def test_has_multiple_dupplicate(self):
        result, number = hasDupplicate([1,2,3,4,2,1,3,4,10,1,2])
        expected = True 
        self.assertEqual(expected, result)
        self.assertEqual(number, [1, 2, 3, 4])

    def test_has_one_dupplicate(self):
        result, number = hasDupplicate([1,2,3,4,5,6,7,8,9,4])
        expected = True
        self.assertEqual(expected, result)
        self.assertEqual(len(number), 1)
        self.assertEqual(number, [4])

    def test_has_every_dupplicate_long(self):
        result, number = hasDupplicate([1,1,1,1,1,1,1,1,1,1])
        expected = True
        self.assertEqual(expected, result)
        self.assertEqual(number, [1])

    def test_has_every_dupplicate_short(self):
        result, number = hasDupplicate([2,2])
        expected = True
        self.assertEqual(expected, result)
        self.assertEqual(number, [2])

    def test_has_no_dupplicate(self):
        result, number = hasDupplicate([1,2,3,4,5,6,7,8,9,10])
        expected = False
        self.assertEqual(expected, result)
        self.assertEqual(number, [])

    def test_has_one_element(self):
        result, number = hasDupplicate([10])
        expected = False 
        self.assertEqual(expected, result)
        self.assertEqual(number, [])

    def test_has_no_element(self):
        result, number = hasDupplicate([])
        expected = False 
        self.assertEqual(expected, result)
        self.assertEqual(number, [])

if __name__ == '__main__':
    unittest.main(verbosity=2)
