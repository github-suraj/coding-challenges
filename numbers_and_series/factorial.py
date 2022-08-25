'''
Program to find factorial of a number
    Ex.- num = 7
        Output -> 5040
'''

from functools import reduce

def factorial_using_recursion(number):
    '''
        Function to find factorial of a number using recursion
    '''
    if number < 0:
        raise ValueError(f"Expected value equal to or greater than zero(0), but got {number}")
    if number == 0:
        return 1
    return number * factorial_using_recursion(number-1)


def factorial_using_iteration(number):
    '''
        Function to find factorial of a number using recursion
    '''
    if number < 0:
        raise ValueError(f"Expected value equal to or greater than zero(0), but got {number}")
    fact = 1
    while number:
        fact *= number
        number -= 1
    return fact


def factorial_using_reduce(number):
    '''
        Function to find factorial of a number using reduce
    '''
    if number < 0:
        raise ValueError(f"Expected value equal to or greater than zero(0), but got {number}")
    if number == 0:
        return 1
    return reduce(lambda a, b: a * b, range(1, number+1))


if __name__ == '__main__':
    for i in range(5):
        print(factorial_using_recursion(i))
        print(factorial_using_iteration(i))
        print(factorial_using_reduce(i))
