#!/usr/bin/env python

"""
Problem:
    Convert the roman number string into his decimal value

    "IV" -> 4, "VI" -> 6, "X" -> 10, "IX" -> 9, "C" -> 100, "III" -> 3

References:
    https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/
"""

class InvalidSymbolError(Exception): pass

def roman(symbols):
    """
    Time O(n)
    Space O(1)
    """

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def value(symbol):
        if symbol not in values:
            raise InvalidSymbolError("{0} is invalid".format(symbol))
        return values.get(symbol, 0)

    result = 0
    size = len(symbols)
    symbols = symbols.upper()

    for i in range(size - 1):
        current_value = value(symbols[i])
        if current_value < value(symbols[i + 1]):
            result -= current_value
        else:
            result += current_value

    # add the last remaining character
    result += value(symbols[size - 1])

    return result

# Test

import unittest

class Test(unittest.TestCase):

    def test_roman(self):
        self.assertEqual(roman('IV'), 4)
        self.assertEqual(roman('VI'), 6)
        self.assertEqual(roman('X'), 10)
        self.assertEqual(roman('XI'), 11)
        self.assertEqual(roman('IX'), 9)
        self.assertEqual(roman('XL'), 40)
        self.assertEqual(roman('LX'), 60)
        self.assertEqual(roman('DCCCXLV'), 845)
        self.assertEqual(roman('MMXIX'), 2019)
        self.assertEqual(roman('C'), 100)

    def test_roman_repeat(self):
        self.assertEqual(roman('III'), 3)
        self.assertEqual(roman('XX'), 20)
        self.assertEqual(roman('LXXX'), 80)

    def test_roman_invalid(self):
        self.assertRaises(InvalidSymbolError, roman, 'YIII')
        self.assertRaises(InvalidSymbolError, roman, 'ABC')

    def test_roman_lower(self):
        self.assertEqual(roman('mcmlxxxiv'), 1984)
        self.assertEqual(roman('mmxix'), 2019)

if __name__ == '__main__':
    unittest.main(verbosity=2)
