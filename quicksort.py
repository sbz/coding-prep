#!/usr/bin/env python

"""
Problem:
    Implement quicksort algorithm on a array

References:
    https://en.wikipedia.org/wiki/Quicksort
    http://www.geeksforgeeks.org/quick-sort
    https://algs4.cs.princeton.edu/23quicksort
"""

import random


def qsort_naive_r(array):
    """
    Time O(n*log(n))
    Space O(log(n))
    """
    left = []
    middle = []
    right = []
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        for i in array:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                middle.append(i)
        left = qsort_naive_r(left)
        right = qsort_naive_r(right)
        return left + middle + right


def qsort_r(array):
    """
    Time O(n*log(n))
    Space O(log(n))
    """
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return qsort_r(left) + [pivot] + qsort_r(right)

if __name__ == '__main__':
    array = [random.randint(i, 20) for i in range(0, 20)]
    array_sorted = qsort_r(array)
    print(array)
    print(array_sorted)
