'''
    Module File for strings functions
'''

from string import ascii_letters

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


def is_substring(string, substring):
    '''
        Check if Substring is Present in a Given String
    '''
    return string.find(substring) != -1


def get_even_length_words(phrase):
    '''
        Python program to find even length words in a phrase
    '''
    words = list()
    for word in phrase.split():
        if len(word) % 2 == 0:
            words.append(word)
    return words


def all_vowels_present(string):
    '''
        Program to check if string contains all vowels
    '''
    vowels = set('aeiou')
    diff = vowels - set(string.lower())
    return len(diff) == 0


def remove_duplicates(string):
    '''
        Remove all duplicates from a given string in Python
             *** Only alphabets will be considered ***
    '''
    unique = ''
    for char in string:
        if char not in ascii_letters:
            continue
        if char.lower() not in unique.lower():
            unique += char
    return unique


def contains_all_unique(string):
    '''
        Python program to check if a string contains all unique characters
    '''
    return len(set(string.lower())) == len(string)


if __name__ == '__main__':
    STR = 'Python is Easy'
    print(f"Reverse of '{STR}' :", reverse(STR))
    print(f"Reverse of '{STR}' :", reverse_phrase(STR))
    print(f"'is' Is Substring of '{STR}':", is_substring(STR, 'is'))
    print(f"'hello' Is Substring of '{STR}':", is_substring(STR, 'hello'))
    print(f"Get Even Length words of '{STR}' :", get_even_length_words(STR))
    print("all vowels present 'hello world!' :", all_vowels_present('hello world!'))
    print("all vowels present 'Hi, how are you?' :", all_vowels_present('Hi, how are you?'))
    print("Remove duplicates 'Malayalam' :", remove_duplicates('Malayalam'))
    print("contains all unique 'malayalam' :", contains_all_unique('malayalam'))
    print("contains all unique 'python' :", contains_all_unique('python'))
