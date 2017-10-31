#!/usr/bin/env python

import sys

"""
Problem:
    Check matching parenthesis balance

References:
    https://en.wikipedia.org/wiki/Dyck_language
    https://eccc.hpi-web.de/report/2009/119/
"""


def check_balance(corpus):
    """
    Time O(n)
    Space O(n)
    """
    corpus = "".join(corpus.split())
    stack = []

    if list(corpus).count('(') != list(corpus).count(')'):
        return False

    for c in corpus:
        if c == '(':
            stack.append(c)
        if c == ')' and len(stack) != 0:
            top = stack[-1]
            if top == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0


def check_balance_space(corpus):
    """
    Time O(n)
    Space O(1)
    """
    corpus = "".join(corpus.split())
    counter = 0

    if list(corpus).count('(') != list(corpus).count(')'):
        return False

    for c in corpus:
        if c == '(':
            counter += 1
        if c == ')':
            if counter == 0:
                return False
            else:
                counter -= 1

    return counter == 0


def main():

    tests = [
        "(good bracket ())",
        "(bad bracket()",
        "((bad bracket again",
        "))((bad bad",
        "((())) good bracket ()",
        "()()()() good bracket",
        "(((((((((())))))))))",
        "((((((((())))))))))",
        "[()()]",
    ]

    for test in tests:
        result = check_balance(test)
        print(test, result)
        result = check_balance_space(test)
        print(test, result)

if __name__ == '__main__':
    sys.exit(main())
