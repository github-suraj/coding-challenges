'''
    Program to Find largest word in a list
    Giving a list and a string,
        find the longest string in list
        which can be formed by deleting some characters of the given 'string'.
    Examples:
        Input:
            list = {"ale", "apple", "monkey", "plea"}
            string = "abpcplea"
        Output:
            apple
'''

def get_largest_word(word_list, string):
    '''
        Function to find largest word in a list
    '''
    largest = ''
    for word in word_list:
        if len(largest) < len(word):
            for char in word:
                if char not in string:
                    break
            else:
                largest = word
    return largest


if __name__ == '__main__':
    words = ["ale", "apple", "monkey", "plea"]
    STRING = "abpcplea"
    print(get_largest_word(words, STRING))
