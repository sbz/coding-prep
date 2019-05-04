#!/usr/bin/env python

"""
Problem:
    Find the matching closing parenthesis at the given index

References:
    https://www.interviewcake.com/question/python3/matching-parens
"""

def get_closing_paren(sentence, opening_paren_index):
    """
    Time O(n)
    Space O(1)
    """

    # Find the position of the matching closing parenthesis
    count = 0
    
    source = sentence[opening_paren_index:]
    if source[0] != '(':
        return -1
    
    for index, c in enumerate(source):
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
            if count == 0:
                return index+opening_paren_index
                
    raise Exception("No closing paren")

def show_closing_paren(source):
    i = len("opening")
    c = len("closing")
    ret = get_closing_paren(source, 10)
    print("opening" + " "*(10-i) + str(10))
    print(" "*10 + "|")
    print(source)
    print(" "*ret + "|")
    print("closing" + " "*(ret-c) + str(ret))

    print("\n\n")
    ret = get_closing_paren(source, 28)
    print("opening" + " "*(28-i) + str(28))
    print(" "*28 + "|")
    print(source)
    print(" "*ret + "|")
    print("closing" + " "*(ret-c) + str(ret))

# Tests

import unittest

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)

    def test_matching_paren_1(self):
        result = get_closing_paren(sentence, 10)
        expected = 79
        self.assertEqual(result, expected)
        
    def test_matching_paren_2(self):
        result = get_closing_paren(sentence, 28)
        expected = 46
        self.assertEqual(result, expected)

if __name__ == '__main__':
    sentence = "Sometimes (when I nest them (my parentheticals)" \
	" too much (like this (and this))) they get confusing"
    show_closing_paren(sentence)
    unittest.main(verbosity=2)
