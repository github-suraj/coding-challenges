'''
    Given a length n,
    Count the number of strings of length n that can be made
        using 'a', 'b' and 'c' with at-most one 'b' and two 'c's allowed.
'''

def count_string_formation(str_len, b_count, c_ount):
    '''
        Function to count the number of strings of length n
    '''
    if b_count < 0 or c_ount < 0:
        return 0
    if str_len == 0 or (b_count == 0 and c_ount == 0):
        return 1
    res = count_string_formation(str_len-1, b_count, c_ount)
    res += count_string_formation(str_len-1, b_count-1, c_ount)
    res += count_string_formation(str_len-1, b_count, c_ount-1)
    return res


if __name__ == '__main__':
    print(count_string_formation(3, 1, 2))
