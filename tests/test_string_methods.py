'''
    Module file for Test Cases for string methods / classes
'''

import unittest
from strings.generate_words_from_random_string import generate_words_from_random_string

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
