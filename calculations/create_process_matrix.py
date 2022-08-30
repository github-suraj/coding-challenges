'''
    Create a function which can be called either way:
        Run1:- create_process_matrix(1,2,3,4,5,6,7,8,9,size=5,diagonal_right="Sum")
            OR
        Run2:- create_process_matrix(1,2,3,4,5,diagonal_right="Sum",diagonal_left="Multiply")
'''

import random
from functools import reduce


def final_result(numbers, operator):
    '''
        Function for arithematic calculation on list of numbers
            Based on type of operation
    '''
    if operator == "Sum":
        return reduce(lambda a, b: a + b, numbers)
    return reduce(lambda a, b: a * b, numbers)


def create_process_matrix(*args, size=4, diagonal_right=None, diagonal_left=None):
    '''
        Create Process Matrix function:
            To Create a matrix of size ( size X size )
            To Calculate Sum or Multiplication of Left/Right Diagonals
    '''
    print("Matrix = ")
    matrix = []
    for _ in range(size):
        row = [random.choice(args) for _ in range(size)]
        matrix.append(row)
        print(row)

    diagonal_left_values = []
    diagonal_right_values = []
    for i in range(size):
        diagonal_left_values.append(matrix[i][i])
        diagonal_right_values.append(matrix[i][size - 1 - i])

    if diagonal_left in ("Sum", "Multiply"):
        diagonal_left_result = final_result(diagonal_left_values, diagonal_left)
        print(f"DiagonalLeft :: {diagonal_left} --> {diagonal_left_result}")

    if diagonal_right in ("Sum", "Multiply"):
        diagonal_right_result = final_result(diagonal_right_values, diagonal_right)
        print(f"DiagonalRight :: {diagonal_right} --> {diagonal_right_result}")


if __name__ == '__main__':
    create_process_matrix(1,2,3,4,5,6,7,8,9, size=5, diagonal_right="Sum")
    create_process_matrix(1,2,3,4,5, diagonal_right="Sum", diagonal_left="Multiply")
