'''
    Module file for Test Cases for dictionary methods / classes
'''

import unittest
from dicts.dict_functions import list_of_tuples_to_dict, add_two_dictionaries

class TestDictsMethods(unittest.TestCase):
    '''
        class for unittesting dictionary methods / classes
    '''
    def test_dict_functions(self):
        '''
            Function to test dictionary functions
        '''
        dict1 = {'A': 72, 'B': 27, 'C': 7, 'D': 53}
        dict2 = {'C': 53, 'D': 42, 'E': 92, 'F': 94}
        list_of_tup = (('A', 72), ('B', 27), ('C', 7), ('D', 53))
        self.assertEqual(list_of_tuples_to_dict(list_of_tup), dict1)
        expected = {'A': 72, 'B': 27, 'C': 53, 'D': 42, 'E': 92, 'F': 94}
        self.assertEqual(add_two_dictionaries(dict1, dict2), expected)
