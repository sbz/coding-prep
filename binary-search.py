#!/usr/bin/env python

import sys
import random
from timeit import Timer

"""
Problem:
    Find integer into a sorted array using binary search algorithm

References:
    https://en.wikipedia.org/wiki/Binary_search_algorithm
"""

def binary_search(array, value):
    """
    Time O(log(n))
    Space O(1)
    """
    left = 0
    right = len(array)
    if array[left] == value:
        return left
    while left <= right:
        mid = int((right-left)/2+left)
        if array[mid] == value:
            return mid
        if value < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_r(array, value, left, right):
    """
    Time O(log(n))
    Space O(1)
    """
    if right < left:
        return -1
    mid = int((right-left)/2+left)
    if array[mid] == value:
        return mid
    if value < array[mid]:
        return binary_search_r(array, value, left, mid - 1)
    else:
        return binary_search_r(array, value, mid + 1, right)


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def binary_search_std(array, value):
    import bisect
    index = bisect.bisect_left(array, value)
    if index != len(array) and array[index] == value:
        return index
    return -1

def main():

    array = [3, 5, 9, 10, 25, 50, 100]
    i = 0
    while i < 500:
        number = random.randint(0, 500)
        array.append(number)
        i += 1

    array = sorted(array)
    print(array)

    start = 0
    end = len(array)

    r = binary_search(array, 1)
    print(r, array[r])
    r = binary_search(array, 25)
    print(r, array[r])
    r = binary_search_r(array, 25, start, end)
    print(r, array[r])
    r = binary_search_std(array, 25)
    print(r, array[r])

    wrapped = wrapper(binary_search, array, 25)
    t = Timer(wrapped)
    print("Binary Search   time: {}".format(t.timeit()))

    wrapped = wrapper(binary_search_r, array, 25, start, end)
    t = Timer(wrapped)
    print("Binary Search R time: {}".format(t.timeit()))

if __name__ == '__main__':
    sys.exit(main())
