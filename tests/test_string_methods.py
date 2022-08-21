'''
    Module file for Test Cases for string methods / classes
'''

import unittest
from strings.generate_words_from_random_string import generate_words_from_random_string
from strings.check_balanced_brackets import is_balanced_brackets

class TestStringMethods(unittest.TestCase):
    '''
        class for unittesting string methods
    '''
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
