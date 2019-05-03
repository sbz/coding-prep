#!/usr/bin/env python

"""
Problem:
    Find the amount of the best profit you can make on stocks efficiently

References:
    https://www.interviewcake.com/question/python3/stock-price
"""

def get_max_profit(stock_prices):
    """
    Time  O(n)
    Space O(1)
    """
    size = len(stock_prices)
    if size < 2:
        raise ValueError("Profit requires at least 2 prices")
   
    max_profit = stock_prices[1] - stock_prices[0]
    lowest_price = stock_prices[0]
    
    # Calculate the max profit
    for i in range(size):
        if stock_prices[i] < lowest_price:
            lowest_price = stock_prices[i]
        best_profit = stock_prices[i] - lowest_price
	# best_profit != 0 avoid to update max_profit when alls going down
        if best_profit > max_profit and best_profit != 0:
            max_profit = best_profit

    return max_profit


# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

if __name__ == '__main__':
    stock_prices = [10, 7, 5, 8, 11, 9]
    max_profit = get_max_profit(stock_prices)
    assert max_profit == 6
    unittest.main(verbosity=2)
