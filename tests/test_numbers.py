'''
    Module file for Test Cases for numbers methods / classes
'''

import random
import unittest
from numbers_and_series.numeric_functions import reverse, format_number
from numbers_and_series.get_missing_number import get_missing_number
from numbers_and_series.prime_numbers import (is_prime, prime_numbers,
    prime_numbers_sieve_method)
from numbers_and_series.fibonacci_numbers import (is_fibonacci_series_number,
    nth_fibonacci_series_number, fibonacci_series)
from numbers_and_series.lucas_numbers import (nth_lucas_series_number,
    lucas_series)
from numbers_and_series.is_armstrong_number import is_armstrong_number
from numbers_and_series.is_palindrome import is_palindrome_number
from numbers_and_series.factorial import (factorial_using_recursion,
    factorial_using_iteration, factorial_using_reduce)
from numbers_and_series.maximum_subarray_sum import (maximum_subarray_sum_old,
    maximum_subarray_sum, maximum_subarray_sum_array)
from numbers_and_series.catalan_numbers import (catalan_numbers,
    get_catalan_numbers)

class TestNumbers(unittest.TestCase):
    '''
        class for unittesting numbers methods / classes
    '''
    def test_numeric_functions(self):
        '''
            Function to test numeric functions
        '''
        self.assertEqual(reverse(123456789), 987654321)
        self.assertEqual(format_number(123456789), '123,456,789')

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

    def test_is_palindrome_number(self):
        '''
            Function to test if a number is palindrome
        '''
        self.assertTrue(is_palindrome_number(12345678987654321))
        self.assertFalse(is_palindrome_number(123456789))

    def test_factorial(self):
        '''
            Function to test factorial of a number
        '''
        # Negative numbers
        with self.assertRaises(ValueError) as context:
            factorial_using_recursion(-10)
        self.assertEqual(str(context.exception),
            "Expected value equal to or greater than zero(0), but got -10")

        with self.assertRaises(ValueError) as context:
            factorial_using_iteration(-5)
        self.assertEqual(str(context.exception),
            "Expected value equal to or greater than zero(0), but got -5")

        with self.assertRaises(ValueError) as context:
            factorial_using_reduce(-1)
        self.assertEqual(str(context.exception),
            "Expected value equal to or greater than zero(0), but got -1")

        # Zero
        self.assertEqual(factorial_using_recursion(0), 1)
        self.assertEqual(factorial_using_iteration(0), 1)
        self.assertEqual(factorial_using_reduce(0), 1)

        # One
        self.assertEqual(factorial_using_recursion(1), 1)
        self.assertEqual(factorial_using_iteration(1), 1)
        self.assertEqual(factorial_using_reduce(1), 1)

        # any number > 1
        self.assertEqual(factorial_using_recursion(5), 120)
        self.assertEqual(factorial_using_iteration(6), 720)
        self.assertEqual(factorial_using_reduce(7), 5040)

    def test_maximum_subarray_sum(self):
        '''
            Function to test maximum subarray sum functions
        '''
        raw = {
            (1, (1,)): [1],
            (6, (4,-1,2,1)): [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            (7, (4, -1, -2, 1, 5)): [-2, -3, 4, -1, -2, 1, 5, -3],
            (23, (5, 4, -1, 7 ,8)): [5, 4, -1, 7 ,8]
        }
        for expected, arr in raw.items():
            self.assertEqual(maximum_subarray_sum_old(arr), expected[0])
            self.assertEqual(maximum_subarray_sum(arr), expected[0])
            self.assertEqual(maximum_subarray_sum_array(arr), expected[1])

    def test_catalan_numbers(self):
        '''
            Function to test catalan numbers methods
        '''
        expected = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
        self.assertEqual(catalan_numbers(10), expected)
        self.assertEqual(get_catalan_numbers(10), expected)
