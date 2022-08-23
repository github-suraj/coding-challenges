'''
    Module file for Test Cases for numbers methods / classes
'''

import random
import unittest
from numbers_and_series.get_missing_number import get_missing_number

class TestNumbers(unittest.TestCase):
    '''
        class for unittesting numbers methods / classes
    '''
    def test_get_missing_number(self):
        '''
            Function to test to find missing number from a list
        '''
        list1 = list(range(1, 101))
        missing_number = list1.pop(random.randrange(1, 100))
        self.assertEqual(get_missing_number(list1), missing_number)
