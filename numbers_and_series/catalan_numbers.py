'''
    Program for nth Catalan Number
    The first few Catalan numbers
        for n = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 … are
                1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
'''


def catalan_decorator(func):
    '''
        Decorator for memoization for reducing time complexity
    '''
    memory = {}
    def inner(num):
        if num not in memory:
            memory[num] = func(num)
        return memory[num]
    return inner


@catalan_decorator
def catalan(num):
    '''
        Recursive Solution with memoization to get nth Catalan numbers
    '''
    if num <= 1:
        return 1

    result = 0
    for i in range(num):
        result += catalan(i) * catalan(num - i - 1)
    return result


def catalan_numbers(num):
    '''
        Function to get first n catalan numbers
    '''
    catalan_nums = []
    for i in range(num):
        catalan_nums.append(catalan(i))
    return catalan_nums


def get_catalan_numbers(num):
    '''
        In this method, we have used boost multi-precision library,
            and the motive behind its use is just only to have precision
            meanwhile finding the large CATALAN's number and
            a generalized tech. using for loop to calculate Catalan numbers.
        Time Complexity:
            O(n)
        Auxiliary Space:
            O(1), since no extra space has been taken.
        Solution:
            prev_cat = 1, when i = 0
            Fn = (prev_cat * (4 * i - 2)) // (i + 1)
                Where i = 1, 2, 3 ...
    '''
    catalan_nums = [1]
    for i in range(1, num):
        cat = (catalan_nums[-1] * (4 * i - 2)) // (i + 1)
        catalan_nums.append(cat)
    return catalan_nums


if __name__ == '__main__':
    print(catalan_numbers(15))
    print(get_catalan_numbers(15))
