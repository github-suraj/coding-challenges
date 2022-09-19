'''
Problem:
    Given an n X n plane,
        how many ways a person can travel from starting cell (yellow)
        to the destination cell (green)
        without stepping into the dangercell(red).

    There is only one danger cell which is always below the destination cell.
    The person can move only 1 step at a time and can only move to right or up.

    Input:
        n - size of the plan (2 <= n <= 20)
    Output:
        number of ways the person can travel

    Test Case 1:
        Input: 3
        Output: 3

    Test Case 2:
        Input: 4
        Output: 7
'''


def number_of_ways_helper(row, col):
    '''
        Helper Function to how many ways a person can travel
    '''
    if row == 0 and col == 0:
        return 1
    if row < 0 or col < 0 or (row == 1 and col == 0):
        return 0
    return number_of_ways_helper(row-1, col) + number_of_ways_helper(row, col-1)


def ways_a_person_can_travel(size):
    '''
        Function to how many ways a person can travel
    '''
    return number_of_ways_helper(size-1, size-1)


if __name__ == '__main__':
    print(ways_a_person_can_travel(3))
    print(ways_a_person_can_travel(4))
