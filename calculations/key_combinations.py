'''
Problem:
    A robbery team went to a city to rob.
    Every house in the city has a number lock with different number of rings.
    Insider information tells them that every key combination is a palindrome.
        ex: 121, 4554.

    How many different combinations they have to check
        for a given lock with n rows?
        For even number of rows, the key starts with an even number
        & for an odd number of rows, the key starts with odd number.

    Input:
        n the number of rings (1 <= n <= 30)
    Output:
        number of keys they have to verify

    Test Case 1:
        Input: 2
        Output: 5
        Explanation:
            as n is even, the key should start with an even number
                and it should be a palindrome.
            So, the possible keys are 00, 22, 44, 66 and 88.

    Test Case 2:
        Input: 3
        Output: 50
        Explanation:
            as n is odd, the key should start with an odd number
                and it should be a palindrome.
            So, the possible keys are 1n1, 3n3, 5n5, 7n7, 9n9
            where n can be from 0 to 9 i.e., 10. So, total 5 times 10 is 50.
'''


def number_of_key_combinations(n):
    '''
        Function to find different combinations robbery team have to check
    '''
    if n % 2 != 0:
        n += 1
    return 5 * (10 ** (n // 2 - 1))


if __name__ == '__main__':
    print(number_of_key_combinations(2))
    print(number_of_key_combinations(3))
