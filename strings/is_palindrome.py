'''
    Programs to check if a string / phrase is palindrome
'''

from string import  ascii_lowercase
from strings_functions import reverse

def is_string_palindrome(string):
    '''
        Function to check if a string is palindrome or not
        (actual string and it's reverse is equal or not)
        Ex.-
            string = 'hello world'
                Output -> False
            string = 'malayalAM'
                Output -> True
    '''
    return string.lower() == reverse(string).lower()


def is_phrase_palindrome(phrase):
    '''
        Method to check if a phrase/sentence is palindrome or not
            *** Only alphabets will be considered ***
        (actual phrase and it's reverse is equal or not)
        Ex. -
            phrase = 'Too hot to hoot.'
                Output -> True
    '''
    phrase = ''.join(filter(lambda char: char in ascii_lowercase, phrase.lower()))
    phrase_len = len(phrase)
    for i in range(phrase_len//2):
        if phrase[i] != phrase[phrase_len-1-i]:
            return False
    return True


if __name__ == '__main__':
    print(is_string_palindrome('hello world'))
    print(is_string_palindrome('malayalAM'))
    print(is_phrase_palindrome('Too hot to hoot.'))
