'''
    Module file for Test Cases for list methods / classes
'''

import unittest
from lists.list_functions import (reverse, swap_elements, numbers_square,
    numbers_cube, list_length, remove_nth_occurrence_from_list,
    is_element_in_list)

class TestListsMethods(unittest.TestCase):
    '''
        class for unittesting list methods / classes
    '''
    def test_list_functions(self):
        '''
            Function to test list functions
        '''
        lst = [6, 9, 3, 7, 1, 2, 8]
        self.assertEqual(reverse(lst), lst[::-1])
        expected = [1, 9, 3, 7, 6, 2, 8]
        self.assertEqual(swap_elements(lst, 0, 4), expected)

        lst = [1, 2, 3, 4]
        self.assertEqual(numbers_square(lst), [(1, 1),(2, 4),(3, 9),(4, 16)])
        self.assertEqual(numbers_cube(lst), [(1, 1),(2, 8),(3, 27),(4, 64)])

        lst = ['python', 'is', 'easy', 'is', 'english', 'is', 'best']
        expected = ['python', 'is', 'easy', 'english', 'is', 'best']
        self.assertEqual(
            remove_nth_occurrence_from_list(lst, 'is', n=2),
            expected
        )
        self.assertEqual(list_length(lst), 6)
        self.assertTrue(is_element_in_list(lst, 'easy'))
        self.assertFalse(is_element_in_list(lst, 'Easy'))
