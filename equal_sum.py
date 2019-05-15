#!/usr/bin/env python

"""
Problem:
    Given an array of integers greater than zero, find if it is possible to
    split it in two such the sum of the two is the same. Print the resulting
    arrays

    [3, 4, 5, 2] -> [3,4] [5, 2]
    [1, 10, 15, 20, 4, 2] -> [1, 10, 15] [20, 4, 2]
    [ 4, 3, 2, 1] -> False, Not possible

References:
    https://www.geeksforgeeks.org/split-array-two-equal-sum-subarrays/
"""



def split_equal_sum(array):
    """
    We test the subarrays from start to index and index to end using the
    slice indexing and return the partition when sum are equal

    Time O(n)
    Space O(1)
    """
    size = len(array)
    if size == 1:
        return False

    def sum_is_equal(array_left, array_right):
        return sum(array_left) == sum(array_right)

    for index in range(size):
        array_left = array[:index+1] # start to index
        array_right = array[index+1:] # index to end
        if sum_is_equal(array_left, array_right):
            return [array_left, array_right]

    return False

def split_equal_sum_alt(array):
    """
    We look for a sum equal to the half sum from start to index and return
    the slice indexing array if we found it or False

    Time O(n)
    Space O(1)
    """
    if len(array) == 1:
        return False

    half_sum = sum(array) / 2
    current_sum = index = 0

    while current_sum < half_sum:
        current_sum += array[index]
        index += 1

    return [array[:index], array[index:]] \
            if current_sum == half_sum else False

def split_equal_sum_alt2(array):
    """
    We use another list and mutate the input array by appending the first
    element in the new array and computing the sum of both arrays

    Time O(n)
    Space O(n)
    """
    if len(array) == 1:
        return False
    splitted = []
    result = False
    while len(array) > 0:
        splitted.append(array[0])
        array.pop(0)
        if sum(array) == sum(splitted):
            result = [array, splitted]
            break
   
    return result

# Test

import unittest

class Test(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(split_equal_sum_alt([3,4,5,2]), [[3,4], [5,2]])
        self.assertEqual(split_equal_sum_alt([1,10,15,20,4,2]), [[1,10,15],
                                                             [20,4,2]])
        self.assertEqual(split_equal_sum_alt([1,2,3]), [[1,2], [3]])
        self.assertEqual(split_equal_sum_alt([1,2,3,4,5,5]), [[1,2,3,4], [5,5]])
        self.assertEqual(split_equal_sum_alt2([8,8]), [[8], [8]])

    def test_invalid(self):
        self.assertFalse(split_equal_sum([4,3,2,1]))
        self.assertFalse(split_equal_sum_alt2([6,4,6,3]))
        self.assertFalse(split_equal_sum_alt([4]))

if __name__ == '__main__':
    unittest.main(verbosity=2)
