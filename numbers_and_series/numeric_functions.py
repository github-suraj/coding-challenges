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


def format_number(number):
    '''
        Write a function named format_number
            that takes a number as its only parameter.
            and convert it to a string with thousands separator (comma).
        For example, calling format_number(1000000) should return "1,000,000".
    '''
    return f"{number:,}"


if __name__ == '__main__':
    print(reverse(123456789))
    print(format_number(1000000))
