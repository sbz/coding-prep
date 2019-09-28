#!/usr/bin/env python
"""
Problem:
    Implement a function to reverse the words in stream. You should do it
    without extra space and linear complexity.

    I have a car -> car a have I
    perfect makes practice -> practice makes perfect
"""

def rev(s):
    result = []
    words = list(s)
    for i in range(len(s)-1, -1, -1):
        result.append(words[i])

    return "".join(result)

def reverse_words(stream_input):
    """
    Use a new array to perform reverse

    Time O(n)
    Space O(n)
    """
    result = []
    rev_words_list = rev(stream_input).split(' ')
    for word in rev_words_list:
        result.append(rev(word))
        result.append(' ')

    return "".join(result)

def reverse_array(input_array, front, tail):
    while front < tail:
        input_array[front], input_array[tail] = \
                input_array[tail], input_array[front]
        front += 1
        tail -= 1

def reverse_words_array(input_array):
    """
    Search for the space and reverse the word one by one in the array
    """
    def index_of(input_array, needle, start):
        for index, value in enumerate(input_array[start:]):
            if value == needle:
                return start+index
        return -1

    current = 0
    while current < len(input_array):
        front = current
        tail = index_of(input_array, ' ', front)
        if tail == -1 or tail == 0:
            reverse_array(input_array, front, len(input_array)-1)
            current = len(input_array)
        else:
            reverse_array(input_array, front, tail-1)
            current = tail+1

def reverse_words_in_place(input_array):
    """
    IN-PLACE reverse without using extra space

    Time O(n)
    Space O(1)

    Aglorithm:
      Reverse all characters in the input_array
      Reverse all words delimited by space in the input_array
    """
    reverse_array(input_array, 0, len(input_array)-1)
    reverse_words_array(input_array)

# Test

import unittest

class Test(unittest.TestCase):

    def test_reverse_words(self):
        self.assertTrue(reverse_words("I have a car"), "car a have I")
        self.assertTrue(reverse_words(list("I have a car")), "car a have I")
        self.assertTrue(reverse_words("perfect makes practice"), 
                        "practice makes perfect")

    def test_reverse_words_in_place(self):
        input_array = list("perfect makes practice")
        reverse_words_in_place(input_array)
        self.assertTrue(input_array, list("pratice makes perfect"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
