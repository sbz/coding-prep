#!/usr/bin/env python

"""
Problem:
    You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1

    Input -> coins = [1, 2, 5], amount = 11
    Output -> 3 (5,5,1)

References:
    https://leetcode.com/problems/coin-change/
"""

def coinChange(coins, amount):
    """
    Ordering the denominations in reversed order help solving it

    Time O(n)
    Space O(n)
    """
    result = {}

    if amount < 0:
        return -1

    for coin in sorted(coins, reverse=True):
        nb = amount // coin
        if coin not in result:
            result[coin] = nb
        amount -= nb * coin
        if amount == 0:
            break

    if amount != 0:
        return -1

    return len(result.keys())

# Test

import unittest

class CoinChangeTest(unittest.TestCase):

    def test_coinChange(self):
        self.assertEqual(coinChange([1,2,5], 11), 3)
        self.assertEqual(coinChange([1,2,4], 6), 2)
        self.assertEqual(coinChange([8], 8), 1)
        self.assertEqual(coinChange([1,2], 3), 2)
        self.assertEqual(coinChange([2], 3), -1)
        self.assertEqual(coinChange([], 1), -1)
        self.assertEqual(coinChange([], -1), -1)
        self.assertEqual(coinChange([4, 3], 7), 2)
        self.assertEqual(coinChange([4], 4), 1)

if __name__ == '__main__':

   unittest.main(verbosity=2)
