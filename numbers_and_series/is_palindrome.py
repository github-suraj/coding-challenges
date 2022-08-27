'''
Program to check if a number is a palindrome number or not
    Ex.-
        num = 12345678987654321
            Output -> True
        num = 1234567
            Output -> False
'''

from numeric_functions import reverse

def is_palindrome_number(number):
    '''
        Function to check if a number is palindrome or not
    '''
    return number == reverse(number)


if __name__ == '__main__':
    print(is_palindrome_number(12345678987654321))
    print(is_palindrome_number(1234567))
