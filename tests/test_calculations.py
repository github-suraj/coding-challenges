'''
    Module file for Test Cases for calculations methods / classes
'''

import unittest
from calculations.students_grade_calculator import Student

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
