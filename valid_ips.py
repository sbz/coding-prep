"""
Problem:
    Validate the IP address in format dot-decimal notation. 
    You must support IPv4 and IPv6 format. 

References:
    https://leetcode.com/problems/validate-ip-address/
    https://www.geeksforgeeks.org/program-to-validate-an-ip-address/
"""

def valid_ipv4_address(numbers):
    for group in numbers:
        if group.startswith('0'):
            return False
        if not 0 <= int(group) <= 255:
            return False
    
    return True

def valid_ipv6_address(numbers):
    hex_values = '0123456789abcedf'
    for group in numbers:
        if len(group) > 4:
            return False
        for digit in list(group):
            if digit.lower() not in hex_values:
                return False
    
    return True

def valid_ip_address(ip_address):
    if '.' in ip_address:
        numbers = ip_address.split('.')
        if len(numbers) != 4: 
            return False
        else:
            return valid_ipv4_address(numbers)
    else:
        numbers = ip_address.split(':')
        if len(numbers) != 8:
            return False
        else:
            return valid_ipv6_address(numbers)
    
    return False

# Test

import unittest

class Test(unittest.TestCase):
    
    def test_ip_v4(self):
        self.assertTrue(valid_ip_address('172.16.254.1'))
        self.assertFalse(valid_ip_address('127.16.254.01'))
        self.assertFalse(valid_ip_address('256.256.256.256'))

    def test_ip_v6(self):
        self.assertTrue(valid_ip_address('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))
        self.assertTrue(valid_ip_address('2001:db8:85a3:0000:0000:8A2E:0370:7334'))
        self.assertTrue(valid_ip_address('2001:db8:85a3:0:0:8A2E:0370:7334'))
        self.assertFalse(valid_ip_address('02001:0db8:85a3:0000:0000:8a2e:0370:7334'))
        self.assertFalse(valid_ip_address('2001:0db8:85a3::8A2E:0370:7334'))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
