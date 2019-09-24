#!/usr/bin/env python
"""
Problem:
    Given an array of integers arr. Write a function flip(arr, k) that reverses
    the order of the first k elements in the array arr. Write a function
    pancake_sort(arr) that sorts and returns the input array. You are allowed to
    use only the function flip() you wrote in the first step in order to make
    changes in the array.

    [1, 5, 3, 4, 2] -> [1, 2, 3, 4, 5]
    [1, 4, 2] -> [1, 2, 4]

References:
    https://www.pramp.com/challenge/3QnxW6xoPLTNl5jX5LM1
    https://en.wikipedia.org/wiki/Pancake_sorting
    https://www.geeksforgeeks.org/pancake-sorting
"""
def find_max_index(array, n):
  """
  Returns index of maximum element in partition array[0..n-1]
  Time O(n)
  Space O(1)
  """
  max_index = 0
  for i in range(n):
    if array[i] > array[max_index]:
      max_index = i

  return max_index

def flip(array, k):
    """
    In-place reverses the k elements in partition array[0..k]
    Time O(k)
    Space O(1)
    """
    index = 0
    while index < k:
      array[index], array[k] = array[k], array[index]
      index += 1
      k -= 1

def pancake_sort(array):
  """
  Performs Pancake sort
  Time O(n^2)
  Space O(1)
  """
  current_size = len(array)
  while current_size > 1:
    max_index = find_max_index(array, current_size)
    if max_index != current_size - 1:
      flip(array, max_index)
      flip(array, current_size - 1)
    current_size -= 1
  
  return array

# Test

import unittest

class Test(unittest.TestCase):
    def test_find_max_index(self):
        assert(find_max_index([6, 8, 19, 1, 2], 5) == 2)
        assert(find_max_index([20, 8, 19, 1, 2], 5) == 0)
        assert(find_max_index([20, 8, 19, 1, 24], 5) == 4)
        assert(find_max_index([20, 8, 19, 100, 24], 5) == 3)

    def test_flip(self):
        l = [10, 5, 3, 2, 1, 6, 9]
        flip(l, 2)
        assert l == [3, 5, 10, 2, 1, 6, 9]

    def test_pancakesort(self):
        assert(pancake_sort([1, 5, 3, 4, 2]) == [1, 2, 3, 4, 5])
        assert(pancake_sort([1, 4, 5, 3, 2, 7]) == [1, 2, 3, 4, 5, 7])
        assert(pancake_sort([1, 4]) == [1, 4])

if __name__ == '__main__':
    unittest.main(verbosity=2)
