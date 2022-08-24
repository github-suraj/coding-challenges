'''
Programs:
    1. To check if a number is fibonacci series number or Not
    2. To find nth fibonacci series number
    3. Find first n fibonacci numbers
'''

import math

def is_perfect_square(num):
    '''
        Function to check if number is a perfect square number
    '''
    sqrt = math.floor(math.sqrt(num))
    return math.pow(sqrt, 2) == num


def is_fibonacci_series_number(num):
    '''
        Function to check if a number is fibonacci series number or Not
            n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or
            both is a perfect square
    '''
    num1 = 5 * num ** 2 + 4
    num2 = 5 * num ** 2 - 4
    return is_perfect_square(num1) or is_perfect_square(num2)


def nth_fibonacci_series_number(n):
    '''
        Function to find nth fibonacci series number
        For example:
            if n = 0, then fib() should return 0.
            If n = 1, then it should return 1.
            For n > 1, it should return Fn-1 + Fn-2
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth_fibonacci_series_number(n-1) + nth_fibonacci_series_number(n-2)


def fibonacci_series(n):
    '''
        Function to find first n fibonacci series numbers
    '''
    fibonacci = []
    a, b = 1, 0
    while n:
        a, b = b, a + b
        fibonacci.append(a)
        n -= 1
    return fibonacci


if __name__ == '__main__':
    for i in range(10):
        print(i, is_fibonacci_series_number(i))
    for i in range(10):
        print(nth_fibonacci_series_number(i), end=' ')
    print('\n', fibonacci_series(10))
