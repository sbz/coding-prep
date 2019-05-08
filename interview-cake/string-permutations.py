#!/usr/bin/env python

import itertools
import unittest

"""
Problem:
    Return all possible permutations of the given string using a recursive
    implementation

References:
    https://www.interviewcake.com/question/python3/recursive-string-permutations
"""

def permutations_string(string):
    """
    Time O(n*2)
    Space O(n)
    """
    # base condition needed to stop recursion
    if len(string) == 0:
        return ['']

    size = len(string)
    # all chars except the first char
    sub_string = string[1:size]
    # we save the first char and will try to put it in every index of the
    # string after retrieving all the substring_permutations
    first_char = string[0]

    substring_permutations = permutations_string(sub_string)
    all_permutations = []
    for permutation in substring_permutations:
        for index in range(0, size):
            new_string = permutation[0:index] \
                            + first_char \
                            + permutation[index:size - 1]
            if new_string not in all_permutations:
                all_permutations.append(new_string)

    return all_permutations

def permutations_string_itertools(string):
   
    all_permutations = []
    for perm_iter in itertools.permutations(string):
        all_permutations.append("".join(perm_iter))

    return all_permutations

# Test

class Test(unittest.TestCase):

    def test_permutation_string(self):
        string = 'cats'
        result = sorted(permutations_string(string))
        expected =  sorted(permutations_string_itertools(string))
        self.assertEqual(result, expected)

    def test_permutation_count(self):
        string = 'cats'
        result = len(sorted(permutations_string(string)))
        expected =  len(sorted(permutations_string_itertools(string)))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
