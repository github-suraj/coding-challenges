'''
    Module file for Test Cases for calculations methods / classes
'''

import unittest
import inspect
from calculations.students_grade_calculator import Student
from calculations.code_analyzer import validate
from calculations.create_process_matrix import (final_result,
    create_process_matrix)

class TestCalculations(unittest.TestCase):
    '''
        class for unittesting calculations methods / classes
    '''
    def test_students_grade_calculator(self):
        '''
            Function to test students grade calculator
        '''
        student = ["Jack Frost", [80, 50, 40, 20], [75, 75], [78.20, 77.20]]
        student_obj = Student(*student)
        self.assertEqual(student_obj.score, 72.79)
        self.assertEqual(student_obj.grade, 'C')

        student = ['Jessica Stone', [67, 55, 77, 21], [40, 50], [69, 44.56]]
        student_obj = Student(*student)
        self.assertEqual(student_obj.score, 48.36)
        self.assertEqual(student_obj.grade, 'E')

        student_obj.calculate_class_result()
        self.assertEqual(student_obj.class_average, 60.58)
        self.assertEqual(student_obj.class_grade, 'D')

    def test_code_analyzer(self):
        '''
            Function to test source code analyzer
        '''
        mycode = inspect.getsource(validate)
        self.assertTrue(validate(mycode))

        mycode = inspect.getsource(final_result)
        self.assertEqual(validate(mycode), "wrong name")

        mycode = inspect.getsource(create_process_matrix)
        self.assertEqual(validate(mycode), "wrong name")
