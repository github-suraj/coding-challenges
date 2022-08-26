'''
    Program to find the sum of the contiguous subarray
        within a one-dimensional array of numbers that has the largest sum.
'''


def maximum_subarray_sum_old(arr):
    '''
        Kadane’s Algorithm to find the sum of the contiguous subarray
    '''
    max_so_far = arr[0]
    max_ending_here = 0
    for num in arr:
        max_ending_here += num
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_ending_here > max_so_far:
            max_so_far = max_ending_here
    return max_so_far


def maximum_subarray_sum(arr):
    '''
        Function to find the sum of the contiguous subarray
    '''
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def maximum_subarray_sum_array(arr):
    '''
        Function to find subarray with maximum sun
    '''
    max_so_far = arr[0]
    max_ending_here = 0
    start = end = count = 0
    for i, num in enumerate(arr):
        max_ending_here += num
        if max_ending_here < 0:
            max_ending_here = 0
            count = i + 1
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = count
            end = i
    return tuple(arr[start: end + 1])


if __name__ == '__main__':
    lst = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maximum_subarray_sum_old(lst))
    print(maximum_subarray_sum(lst))
    print(maximum_subarray_sum_array(lst))
