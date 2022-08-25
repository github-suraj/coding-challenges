'''
Program to check if a number is a armstrong number or not
    Ex.- num = 1634
        number of digits = 4
        new_num = 1**4 + 6**4 + 3**4 + 4**4
        num == new_num
'''

from functools import reduce

def is_armstrong_number(num):
    '''
        Function to check if a number is armstrong number
    '''
    digits = []
    orig_num = num
    while num:
        (num, rem) = divmod(num, 10)
        digits.append(rem)

    num_len = len(digits)
    new_num = reduce(lambda a, b: a + b, map(lambda x: x ** num_len, digits))
    return orig_num == new_num

if __name__ == '__main__':
    nums = [9, 1634, 2345]
    for num1 in nums:
        print(num1, is_armstrong_number(num1))
