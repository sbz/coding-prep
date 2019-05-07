"""
Problem:
    Find if a pattern (sub matrix) exist in a 2D array (matrix)
"""

matrix = [
    [1,2,3,1,1],
    [2,3,4,1,1],
    [3,4,5,6,7],
    [4,5,6,'A',1],
    [5,6,7,'B',1]
]

class Found(Exception): pass

def confirm_existing_pattern(y, x, pattern):
    for yy in range(0, len(pattern)):
        for xx in range(0, len(pattern[0])):
            if pattern[yy][xx] != matrix[yy + y][xx + x]:
                return False
            
    return True

def find_pattern(matrix, pattern):
    """
    Time O(n^2)
    Space O(1)
    """
    try:
        result = [-1,-1]
        
        if pattern is None \
                or len(pattern) == 0 \
                or pattern[0] is None \
                or len(pattern[0]) == 0:
            return result
                
        
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[0])):
                if matrix[y][x] == pattern[0][0]: # we found a match
                    if confirm_existing_pattern(y, x, pattern):
                        result[0] = y
                        result[1] = x
                        raise Found
    except Found:
        return result
    else:
        return [-1,-1]

# Test

import unittest
    
class Test(unittest.TestCase):
    
    def test_pattern_1(self):
        pattern1 = [ [2, 3],[3, 4] ]
        result = find_pattern(matrix, pattern1)
        excepted = [0, 1]
        self.assertEqual(result, excepted)
        
    def test_pattern_2(self):
        pattern1 = [ [1, 1],[1, 1] ]
        result = find_pattern(matrix, pattern1)
        excepted = [0, 3]
        self.assertEqual(result, excepted)
        
    def test_pattern_3(self):
        pattern1 = [ ['A', 1],['B', 1] ]
        result = find_pattern(matrix, pattern1)
        excepted = [3, 3]
        self.assertEqual(result, excepted)
        
    def test_pattern_not_found(self):
        pattern1 = [ [0, 0],[0, 0] ]
        result = find_pattern(matrix, pattern1)
        excepted = [-1, -1]
        self.assertEqual(result, excepted)
    
    def test_pattern_empty_1(self):
        pattern1 = [ [],[] ]
        result = find_pattern(matrix, pattern1)
        excepted = [-1, -1]
        self.assertEqual(result, excepted)
        
    def test_pattern_empty_2(self):
        pattern1 = [ ]
        result = find_pattern(matrix, pattern1)
        excepted = [-1, -1]
        self.assertEqual(result, excepted)
        
    def test_pattern_not_number(self):
        pattern1 = [ ['A', 1], ['B', 2] ]
        result = find_pattern(matrix, pattern1)
        excepted = [-1, -1]
        self.assertEqual(result, excepted)
    
    def test_pattern_none_1(self):
        pattern1 = [ [None, 1], ['B', 2] ]
        result = find_pattern(matrix, pattern1)
        excepted = [-1, -1]
        self.assertEqual(result, excepted)
    
    def test_pattern_none_2(self):
        pattern1 = None
        result = find_pattern(matrix, pattern1)
        excepted = [-1, -1]
        self.assertEqual(result, excepted)
    
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
