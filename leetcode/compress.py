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
    OrderedDict needed to keep the order of the char in the string

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


def compress_string_alt(string):
    """
    Another way to do it without OrderedDict

    Time O(n)
    Space O(n)
    """
    def compress_format_chars(prev_char, count):
        return "{0}{1}".format(prev_char, count) if count > 1 else prev_char

    if string is None or not string:
        return string

    compressed = ""
    count = 0
    prev_char = string[0]
    for char in string:
        if char == prev_char:
            count += 1
        else:
            compressed += compress_format_chars(prev_char, count)
            prev_char = char
            count = 1
    compressed += compress_format_chars(prev_char, count)
    if len(compressed) > len(string):
        return string

    return compressed

# Test

import unittest

class Test(unittest.TestCase):

    def test_stream_none(self):
        stream = None
        result = compress_string_alt(stream)
        expected = None
        self.assertEqual(result, expected)

    def test_stream(self):
        stream = "AAAABCCDDDD"
        result = compress_string_alt(stream)
        expected = "A4BC2D4"
        self.assertEqual(result, expected)

    def test_stream_lowercase(self):
        stream = "AAAABCCDDDD"
        result = compress_string_alt(stream)
        expected = "A4BC2D4"
        self.assertEqual(result, expected)

    def test_stream_mixedcase(self):
        stream = "AAaaaBCCdDDDD"
        result = compress_string_alt(stream)
        expected = "A2a3BC2dD4"
        self.assertEqual(result, expected)

    def test_stream_non_need_compress(self):
        stream = "ABC"
        result = compress_string_alt(stream)
        expected = "ABC"
        self.assertEqual(result, expected)

    def test_stream_empty(self):
        stream = ""
        result = compress_string_alt(stream)
        expected = ""
        self.assertEqual(result, expected)

    def test_stream_one_char(self):
        stream = "Z"
        result = compress_string_alt(stream)
        expected = "Z"
        self.assertEqual(result, expected)

    def test_stream_two_char(self):
        stream = "ZZ"
        result = compress_string_alt(stream)
        expected = "Z2"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
