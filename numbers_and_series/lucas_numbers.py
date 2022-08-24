'''
Programs:
    1. To find nth lucas series number
    2. Find first n lucas numbers
'''


def nth_lucas_series_number(n):
    '''
        Function to find nth lucas series number
        For example:
            if n = 0, then lucas() should return 2.
            If n = 1, then it should return 1.
            For n > 1, it should return Fn-1 + Fn-2
    '''
    if n == 0:
        return 2
    if n == 1:
        return 1
    return nth_lucas_series_number(n-1) + nth_lucas_series_number(n-2)


def lucas_series(n):
    '''
        Function to find first n lucas series numbers
    '''
    lucas = []
    a, b = 2, 1
    while n:
        lucas.append(a)
        a, b = b, a + b
        n -= 1
    return lucas


if __name__ == '__main__':
    for i in range(10):
        print(nth_lucas_series_number(i), end=' ')
    print('\n', lucas_series(10))
