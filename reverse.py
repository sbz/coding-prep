#!/usr/bin/env python

"""
Problem:
    Reverse the input stream

    Input -> Output
    Python is cool -> looC si nohtyP
"""

def rev(stream):
    """
    Iterate backward from last to first index with negative step.

    Time O(n)
    Space O(n)
    """
    stream_list = list(stream)
    result = []
    for i in range(len(stream)-1, 0, -1):
        result.append(stream_list[i])

    result.append(stream_list[0])
    return "".join(result)

def rev_alt(stream):
    """
    Python string are immutables, so use a list to do it IN-PLACE.

    Time O(n)
    Space O(1)
    """
    stream = list(stream)
    size = len(stream)
    for i in range(size // 2):
        stream[i], stream[size - 1 - i] = stream[size - 1 - i], stream[i]

    return "".join(stream)

def rev_slice(stream):
    """
    Time O(n)
    Space O(1)
    """
    return stream[::-1]

# Test

import unittest

class Test(unittest.TestCase):

    def test_reverse(self):
        stream = "Python is cool"
        result = rev(stream)
        expected = rev_slice(stream)
        self.assertEqual(result, expected)

    def test_reverse_alt(self):
        stream = "Python is cool"
        result = rev_alt(stream)
        expected = rev_slice(stream)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
