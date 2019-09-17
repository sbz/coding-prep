#!/usr/bin/env python

"""
Problem:
    Given a array Z of 0s and 1s, divide the array into 3 non-empty parts such
    that all of these parts represents the same binary value.

    If it is possible, return [i, j], such that:
        Z[0], Z[1], ..., Z[i] is the first part
        Z[i+1], Z[i+2], ..., Z[j-1] is the 2nd part
        Z[j], Z[j+1], ..., Z[Z.length -1] is the 3rd part
    If it is not possible, return [-1, -1].

    Input -> Output
    [1, 0, 1, 0, 1] -> [0, 3] -> [1], [0, 1], [0, 1]
    [1, 1, 0, 1, 1] -> [-1, -1]

References:
    https://www.geeksforgeeks.org/divide-binary-array-into-three-equal-parts-with-same-value/
"""

def count_ones_per_partition(array, one_per_part, start=0):
    i = start
    count_ones = 0
    while i < len(array) - 1 and count_ones != one_per_part:
        if array[i] == 1:
            count_ones += 1
        i += 1
    return i

def binary_parts(array, debug=False):
    """
    We need to count the number of 1s per partition to found i and j. Then for
    each partition we lookup the right number of 1s.

    Time O(n)
    Space O(1)
    """
    if debug:
        index_line = "\n"
        val_line = ""
        for idx, val in enumerate(array):
            index_line += " {0} ".format(idx)
            val_line += " {0} ".format(val)
        print(index_line)
        print(val_line)
        
    number_of_ones = array.count(1)
    if number_of_ones % 3 != 0:
        return [-1, -1]
    
    one_per_part = number_of_ones // 3
    i = count_ones_per_partition(array, one_per_part, start=0)
    # found i
    j = count_ones_per_partition(array, one_per_part, start=i)
    # found j
    
    if debug:
        print(array[0:i], array[i:j], array[j:len(array)])

    return [i-1, j]

# Test

import unittest

class Test(unittest.TestCase):
    
    def test_binary_parts(self):
        assert binary_parts([1, 0, 1, 0, 1]) == [0, 3]
        assert binary_parts([1, 1, 0, 1, 1, 0, 1, 1, 0]) == [1, 5]
        assert binary_parts([0, 1, 1, 1, 1, 0, 0, 1, 1]) == [2, 5]
        assert binary_parts([1, 1, 1, 1, 1, 1]) == [1, 4]
        assert binary_parts([1, 0, 0, 1, 0, 1], True) == [0, 4]

    def test_no_binary_parts(self):
        assert binary_parts([1, 0, 1]) == [-1, -1]
        assert binary_parts([1, 1, 1, 1]) == [-1, -1]

if __name__ == '__main__':
    unittest.main(verbosity=2)
