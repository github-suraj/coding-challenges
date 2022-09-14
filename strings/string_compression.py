'''
    Given an string of characters, compress it using the following algorithm:
        Begin with an empty string s.
            For each group of consecutive repeating characters in string:
            1. If the group's length is 1, append the character to s.
            2. Otherwise, append the character followed by the group's length.
        Return The compressed string s
    Input: hello
        Output: hel2o
    Input: aaabbcdda
        Output: a3b2cd2a
'''


def compression(string):
    '''
        Function to compress string of characters
    '''
    new_string = ''
    i = 0
    while i < len(string):
        count = 1
        char = string[i]
        for j in range(i+1, len(string)):
            if char == string[j]:
                count += 1
            else:
                break
        i += count
        new_string += char
        if count > 1:
            new_string += str(count)
    return new_string


if __name__ == '__main__':
    print(compression('hello'))
    print(compression('aaabbcdda'))
