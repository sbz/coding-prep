#!/usr/bin/env python

import collections

"""
Problem:
    Compress a string such that "AAAABCCDDDD" becomes "A4BC2D4". Only
    compress the string if it saves space.

References:
    https://leetcode.com/problems/string-compression/
    https://medium.com/algorithms-practice/string-compression-2269b2ceaac1
"""

def compress_string(string):
    """
    Time O(n)
    Space O(n)
    """
    if string is None:
        return None

    count = collections.OrderedDict()
    for index, c in enumerate(string):
        if c not in count:
            count[c] = 1
        else:
            count[c] = count[c] + 1

    # build compressed string
    compressed = ""
    for char in count:
            if count[char] == 1:
                compressed += "{0}".format(char)
            else:    
                compressed += "{0}{1}".format(char, count[char])

    if len(compressed) > len(string):
        return string

    return compressed

# Test

import unittest

class Test(unittest.TestCase):

    def test_stream_none(self):
        stream = None
        result = compress_string(stream)
        expected = None
        self.assertEqual(result, expected)

    def test_stream(self):
        stream = "AAAABCCDDDD"
        result = compress_string(stream)
        expected = "A4BC2D4"
        self.assertEqual(result, expected)

    def test_stream_lowercase(self):
        stream = "AAAABCCDDDD"
        result = compress_string(stream)
        expected = "A4BC2D4"
        self.assertEqual(result, expected)

    def test_stream_mixedcase(self):
        stream = "AAaaaBCCdDDDD"
        result = compress_string(stream)
        expected = "A2a3BC2dD4"
        self.assertEqual(result, expected)

    def test_stream_non_need_compress(self):
        stream = "ABC"
        result = compress_string(stream)
        expected = "ABC"
        self.assertEqual(result, expected)

    def test_stream_empty(self):
        stream = ""
        result = compress_string(stream)
        expected = ""
        self.assertEqual(result, expected)

    def test_stream_one_char(self):
        stream = "Z"
        result = compress_string(stream)
        expected = "Z"
        self.assertEqual(result, expected)

    def test_stream_two_char(self):
        stream = "ZZ"
        result = compress_string(stream)
        expected = "Z2"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
