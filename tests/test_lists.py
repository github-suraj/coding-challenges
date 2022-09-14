'''
    Module file for Test Cases for list methods / classes
'''

import unittest
from lists.list_functions import (reverse, swap_elements, numbers_square,
    numbers_cube, list_length, remove_nth_occurrence_from_list,
    is_element_in_list, list_xor, arrange_numbers)
from lists.maximum_square_submatrix import maximum_square_submatrix
from lists.maximum_rectangular_submatrix_area import (
    maximum_rectangular_submatrix_area
)
from lists.largest_word import get_largest_word
from lists.check_employee_entry_time import check_employee_entry_time

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
        self.assertTrue(list_xor(1, [1, 2, 3], [4, 5, 6]))
        self.assertTrue(list_xor(1, [0, 2, 3], [1, 5, 6]))
        self.assertFalse(list_xor(1, [1, 2, 3], [1, 5, 6]))
        self.assertFalse(list_xor(1, [0, 0, 0], [4, 5, 6]))
        list1 = [20, 3.5, 10, 4.2, -20 , 100, 27, -10, 35, 3.1, 1, -5]
        expected = [-20, -10, -5, 20, 3.5, 10, 4.2, 100, 27, 35, 3.1, 1]
        self.assertEqual(arrange_numbers(list1), expected)

    def test_maximum_square_submatrix(self):
        '''
            Function to test maximum square submatrix
        '''
        get_expected = lambda length: [[1] * length] * length
        lst = [
            [0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]
        ]
        self.assertEqual(maximum_square_submatrix(lst), get_expected(3))

        lst = [
            [1, 0, 1, 0], [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 0]
        ]
        self.assertEqual(maximum_square_submatrix(lst), get_expected(2))

    def test_maximum_rectangular_submatrix_area(self):
        '''
            Function to test maximum rectangular submatrix area
        '''
        lst = [
            [0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]
        ]
        self.assertEqual(maximum_rectangular_submatrix_area(lst), 8)

        lst = [
            [0, 1, 1], [1, 1, 1], [0, 1, 1]
        ]
        self.assertEqual(maximum_rectangular_submatrix_area(lst), 6)


    def test_largest_word(self):
        '''
            Function to test finding largest word in a list
        '''
        words = ["ale", "applepae", "monkey", "apple", "plea"]
        self.assertEqual(get_largest_word(words, 'abpcplea'), 'applepae')

    def test_check_employee_entry_time(self):
        '''
            Function to test employee entry time checker
        '''
        input1 = ["cris", "peter", "gorge", "Hendry", "jatin", "cris", "Hendry", "Malik", "peter"]
        input2 = ["11:30", "12:10", "14:00", "16:00", "10:40", "12:00", "15:40", "15:30", "16:00"]
        expected = ["cris", "Hendry"]
        self.assertEqual(check_employee_entry_time(input1, input2), expected)
