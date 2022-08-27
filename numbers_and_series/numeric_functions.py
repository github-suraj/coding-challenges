'''
    Module File for numeric functions
'''


def reverse(number):
    '''
        Function to Reverse a Number
    '''
    _number = 0
    while number:
        (number, rem) = divmod(number, 10)
        _number = _number * 10 + rem
    return _number


if __name__ == '__main__':
    print(reverse(123456789))
