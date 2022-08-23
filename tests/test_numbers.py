'''
    Module file for Test Cases for numbers methods / classes
'''

import random
import unittest
from numbers_and_series.get_missing_number import get_missing_number
from numbers_and_series.prime_numbers import (is_prime, prime_numbers,
    prime_numbers_sieve_method)

class TestNumbers(unittest.TestCase):
    '''
        class for unittesting numbers methods / classes
    '''
    def test_get_missing_number(self):
        '''
            Function to test to find missing number from a list
        '''
        list1 = list(range(1, 101))
        missing_number = list1.pop(random.randrange(1, 100))
        self.assertEqual(get_missing_number(list1), missing_number)

    def test_prime_numbers(self):
        '''
            Function to test prime numbers methods
        '''
        self.assertTrue(is_prime(7919))
        self.assertFalse(is_prime(7921))

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
            41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(prime_numbers(2, 100), primes)
        self.assertEqual(prime_numbers_sieve_method(1, 100), primes)
