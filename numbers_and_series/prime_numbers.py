'''
Programs:
    1. To check if a number is Prime or Not
    2. Find all prime numbers between two numbers
'''

import math

def is_prime(num):
    '''
        Function to check if a number is a prime number or not
    '''
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    min_div = math.floor(math.sqrt(num)) + 1
    for i in range(3, min_div, 2):
        if num % i == 0:
            return False
    return True


def prime_numbers(start, end):
    '''
        Function to fetch prime numbers between start and end
    '''
    primes = []
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)
    return primes


def prime_numbers_sieve_method(start, end):
    '''
        Sieve Method to fetch prime numbers between start and end
    '''
    if start < 2:
        start = 2

    primes = [True for _ in range(end+1)]
    point = 2
    while point * point < end:
        if primes[point]:
            for i in range(point * point, end+1, point):
                primes[i] = False
        point += 1
    return [i for i, value in enumerate(primes) if value and i >= start]


if __name__ == '__main__':
    print(prime_numbers(1, 100))
    print(prime_numbers_sieve_method(1, 100))
