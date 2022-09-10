'''
    Count Possible Decodings of a given Digit Sequence
    Let 1 represent 'A', 2 represents 'B', etc.
        Given a digit sequence,
        count the number of possible decodings of the given digit sequence.
    Examples:
        Input:  digits[] = "121"
        Output: 3
            // The possible decodings are "ABA", "AU", "LA"

        Input: digits[] = "1234"
        Output: 3
            // The possible decodings are "ABCD", "LCD", "AWD"
'''


def possible_decodings_helper(string, n):
    '''
        helper function to Count Possible Decodings
    '''
    if n in (0, 1):
        return 1

    count = 0
    if string[n-1] > '0':
        count = possible_decodings_helper(string, n-1)
    if string[n-2] == '1' or (string[n-2] == '2' and string[n-1] < '7'):
        count += possible_decodings_helper(string, n-2)
    return count


def count_possible_decodings(string):
    '''
        function to Count Possible Decodings of a given Digit Sequence
    '''
    if len(string) == 0 or (len(string) == 1 and string[0] == '0'):
        return 0
    return possible_decodings_helper(string, len(string))


if __name__ == '__main__':
    print(count_possible_decodings("121"))
    print(count_possible_decodings("1234"))
