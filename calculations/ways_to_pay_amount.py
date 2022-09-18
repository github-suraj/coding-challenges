'''
Problem:
    In how many ways you can pay N rupees with
    1 rupee, 2 rupee & 5 rupee denominations, In such a way that
        a. number of 1 rupee coins always greater than that of 2 rupee coins.
        b. number of 2 rupee coins always greater than that of 5 rupee coins.
        c. At least one coin should be given from each denomination.

    Input:
        N the amount in rupees (1 <= N <= 100)
    Output:
        the number of ways in which you can pay the amount as described

    Test case 1:
        Input: 10
        Output: 0

    Test case 2:
        Input: 15
        Output: 2
        Explanation:
            Possible ways in which you can pay 15 rupees are
            (1 5rs, 2 2rs, 6 1rs) and (1 5rs, 3 2rps, 4 1rps).
'''


def ways_to_pay_amount(total):
    '''
        Function to fing how many ways you can pay N rupees with
            1 rupee, 2 rupee & 5 rupee denominations
    '''
    if total < 12:
        return 0

    ways = []
    rupees5, rupees2 = 1, 2
    rupees1 = total - (rupees5 * 5) - (rupees2 * 2)
    initial = [rupees5, rupees2, rupees1]
    while initial[0] < initial[1] < initial[2]:
        while initial[0] < initial[1] < initial[2]:
            ways.append(initial.copy())
            initial[1] += 1
            initial[2] -= 2
        rupees5 += 1
        rupees2 += 1
        rupees1 = total - (rupees5 * 5) - (rupees2 * 2)
        initial = [rupees5, rupees2, rupees1]
    return len(ways)


if __name__ == '__main__':
    print(ways_to_pay_amount(10))
    print(ways_to_pay_amount(15))
    print(ways_to_pay_amount(20))
