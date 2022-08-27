'''
    Module File for strings functions
'''


def reverse(string):
    '''
        Function to Reverse a string
    '''
    _string = ''
    for i in range(len(string)):
        _string += string[len(string) - 1 -i]
    return _string


def reverse_phrase(phrase):
    '''
        Function to Reverse phrase
    '''
    return ' '.join(phrase.split()[::-1])


if __name__ == '__main__':
    print(reverse('Python is Easy'))
    print(reverse_phrase('Python is Easy'))
