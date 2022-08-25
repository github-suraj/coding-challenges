'''
    Module file for Test Cases for numbers methods / classes
'''

import random
import unittest
from numbers_and_series.get_missing_number import get_missing_number
from numbers_and_series.prime_numbers import (is_prime, prime_numbers,
    prime_numbers_sieve_method)
from numbers_and_series.fibonacci_numbers import (is_fibonacci_series_number,
    nth_fibonacci_series_number, fibonacci_series)
from numbers_and_series.lucas_numbers import (nth_lucas_series_number,
    lucas_series)
from numbers_and_series.is_armstrong_number import is_armstrong_number

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

    def test_fibonacci_numbers(self):
        '''
            Function to test fibonacci numbers methods
        '''
        self.assertTrue(is_fibonacci_series_number(34))
        self.assertFalse(is_fibonacci_series_number(44))

        self.assertEqual(nth_fibonacci_series_number(10), 55)

        fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fibonacci_series(10), fibonacci)

    def test_lucas_numbers(self):
        '''
            Function to test lucas numbers methods
        '''
        self.assertEqual(nth_lucas_series_number(10), 123)

        lucas = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
        self.assertEqual(lucas_series(10), lucas)

    def test_is_armstrong_number(self):
        '''
            Function to test if a number is armstrong
        '''
        self.assertTrue(is_armstrong_number(9))
        self.assertFalse(is_armstrong_number(2345))
        self.assertTrue(is_armstrong_number(1634))
