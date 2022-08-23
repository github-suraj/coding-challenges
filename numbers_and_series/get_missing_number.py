'''
Program to Find missing number from a list of first n natural numbers
    list = range(1, 100)
    list.remove(58)'
        output -> 58
'''

import random

def get_missing_number(arr):
    '''
        Function to get missing number from a list
    '''
    n = len(arr)
    total = (n + 1) * (n + 2) // 2
    return total - sum(arr)


if __name__ == '__main__':
    listA = list(range(1, 101))
    random.shuffle(listA)
    listA.remove(58)
    num = get_missing_number(listA)
    print(num)
