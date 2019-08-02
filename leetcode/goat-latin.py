#!/usr/bin/env python

"""
Problem: 
    Given the input sentence, convert it to Goat Latin language

References:
    https://leetcode.com/problems/goat-latin/
"""

def goat_latin(sentence):
    """
    Time O(n)
    Space O(n)
    """
    result = ""
    vowels = 'aeiou'

    for index, word in enumerate(sentence.split()):
        if word[0].lower() in vowels:
            result += word + 'ma'
        else:
            first = word[0]
            result += word[1:] + first + 'ma'
        result += 'a' * (index+1)
        result += " "

    return result[0:-1]

# Test

import unittest

class Test(unittest.TestCase):
    def test_goat_latin(self):
        self.assertEqual("Imaa peaksmaaa oatGmaaaa atinLmaaaaa",
                         goat_latin("I speak Goat Latin"))
        self.assertEqual("bzSmaa peakssmaaa oatGmaaaa atinLmaaaaa",
                         goat_latin("Sbz speaks Goat Latin"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
