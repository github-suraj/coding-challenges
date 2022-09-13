'''
    Module file for Test Cases for string methods / classes
'''

import unittest
from strings.strings_functions import (reverse, reverse_phrase, is_substring,
    get_even_length_words, all_vowels_present, remove_duplicates,
    contains_all_unique, capital_indexes)
from strings.generate_words_from_random_string import generate_words_from_random_string
from strings.check_balanced_brackets import is_balanced_brackets
from strings.is_palindrome import is_string_palindrome, is_phrase_palindrome
from strings.count_possible_decodings import count_possible_decodings
from strings.string_formation_count import count_string_formation

class TestStringMethods(unittest.TestCase):
    '''
        class for unittesting string methods
    '''
    def test_strings_functions(self):
        '''
            Function to test strings functions
        '''
        str1 = 'Python is easy'
        self.assertEqual(reverse(str1), 'ysae si nohtyP')
        self.assertEqual(reverse_phrase(str1), 'easy is Python')
        self.assertTrue(is_substring(str1, 'is'))
        self.assertFalse(is_substring(str1, 'Is'))
        self.assertEqual(get_even_length_words(str1), ['Python', 'is', 'easy'])
        self.assertTrue(all_vowels_present('Hi, how are you?'))
        self.assertFalse(all_vowels_present('hello world!'))
        self.assertEqual(remove_duplicates('Malayalam'), 'Maly')
        self.assertTrue(contains_all_unique('python'))
        self.assertFalse(contains_all_unique('malayalam'))
        self.assertEqual(capital_indexes('HeLlO'), [0, 2, 4])

    def test_generate_words_from_random_string(self):
        '''
            Function to test Generate words from random string
        '''
        word_list = ["cat","baby","dog","giraffe","man"]
        self.assertEqual(generate_words_from_random_string(word_list, 'tbdcgaianm'), ['cat', 'man'])
        self.assertEqual(generate_words_from_random_string(word_list, 'bsaysad'), None)
        self.assertEqual(generate_words_from_random_string(word_list, 'aobdcgt'), ['cat', 'dog'])

    def test_is_balanced_brackets(self):
        '''
            Function to test if string is having balanced open and closed brackets
        '''
        self.assertTrue(is_balanced_brackets('{}{[]}'))
        self.assertTrue(is_balanced_brackets('{Suraj}{[Jaiswal]}'))
        self.assertFalse(is_balanced_brackets('{Suraj[}]{Jaiswal}'))
        self.assertFalse(is_balanced_brackets('{[{]}}'))

    def test_is_palindrome(self):
        '''
            Function to test if a string / phrase is palindrome
        '''
        self.assertTrue(is_string_palindrome('malayalAM'))
        self.assertFalse(is_string_palindrome('hello world'))
        self.assertTrue(is_phrase_palindrome('Too hot to hoot.'))
        self.assertFalse(is_phrase_palindrome('hello world'))

    def test_count_possible_decodings(self):
        '''
            Function to test possible decoding counts for sequence of digits
        '''
        self.assertEqual(count_possible_decodings('12321'), 6)
        self.assertEqual(count_possible_decodings('121'), 3)
        self.assertEqual(count_possible_decodings('1234'), 3)

    def test_string_formation_count(self):
        '''
            Function to test to count the number of strings of length n
        '''
        self.assertEqual(count_string_formation(4, 1, 2), 39)
