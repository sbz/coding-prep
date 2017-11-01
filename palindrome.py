#!/usr/bin/env python

import re
import sys
import timeit

"""
Problem:
    Given a string check if it is a palindrome by ignoring spaces

References:
    https://en.wikipedia.org/wiki/Palindrome
"""


def is_palindrome(text):
    """
    Time O(2n)
    """
    text = "".join([c for c in text if c.isalpha()])

    text_reversed = "".join(reversed(text))

    return text == text_reversed


def is_palindrome_fast(text):
    """
    Time O(n)
    """
    if not text or len(text) == 1:
        return False

    text = re.sub(r"[^a-zA-Z]", "", text)
    start = 0
    end = len(text) - 1
    while start < end:
        if text[start].lower() != text[end].lower():
            return False
        start += 1
        end -= 1

    return True


def bench_it(func_str, param_str):
    t = timeit.timeit("{0}{1}".format(func_str, param_str), number=10000)
    sys.stdout.write("bench {0:>14} {1:.16f}".format(func_str, t))
    sys.stdout.write("\n")

if __name__ == '__main__':

    entries = [
        "kayak",
        "lebel",
        "coloc",
        "pop",
        "sbz",
        "sofian",
        "python",
        "lol",
        "!a la m al a!",
        "a man, a plan, a canal, panama!",
        "amanaplanacanalpanama",
        "race car"
    ]

    for entry in entries:
        print("{} {}".format(entry, is_palindrome(entry)))

    for entry in entries:
        print("{} {}".format(entry, is_palindrome_fast(entry)))

    print(timeit.timeit("is_palindrome_fast('race car')",
                        setup="from __main__ import is_palindrome_fast",
                        number=10000))
    print(timeit.timeit("is_palindrome('race car')",
                        setup="from __main__ import is_palindrome",
                        number=10000))
