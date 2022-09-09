'''
    Given a binary matrix,
        find the maximum size rectangle binary-sub-matrix with all 1’s. 
        For example, consider the below binary matrix.
            +---+---+---+---+
            | 0 | 1 | 1 | 0 |
            +---+---+---+---+
            | 1 | 1 | 1 | 1 |
            +---+---+---+---+
            | 1 | 1 | 1 | 1 |
            +---+---+---+---+
            | 1 | 1 | 0 | 0 |
            +---+---+---+---+
        Output:
            8
        Rectangle binary-sub-matrix:
            +---+---+---+---+
            | 1 | 1 | 1 | 1 |    # Row 1 Coulumn 0-1-2-3
            +---+---+---+---+
            | 1 | 1 | 1 | 1 |    # Row 2 Coulumn 0-1-2-3
            +---+---+---+---+
'''

def __max_area(row, temp_array, i, max_area):
    top_val = row[temp_array.pop()]
    area = top_val * i
    if temp_array:
        area = top_val * (i - temp_array[-1] - 1)
    return max(area, max_area)


def get_max_area(row):
    '''
        Function to fetch max area for row
    '''
    temp_array = []
    max_area = i = 0

    while i < len(row):
        if len(temp_array) == 0 or row[temp_array[-1]] <= row[i]:
            temp_array.append(i)
            i += 1
        else:
            max_area = __max_area(row, temp_array, i, max_area)

    while temp_array:
        max_area = __max_area(row, temp_array, i, max_area)

    return max_area


def maximum_rectangular_submatrix_area(array):
    '''
        Function to find maximum size rectangle binary-sub-matrix with all 1's
    '''
    rows = len(array)
    columns = len(array[0])
    result = get_max_area(array[0])

    for i in range(1, rows):
        for j in range(columns):
            if array[i][j]:
                array[i][j] += array[i-1][j]
        result = max(result, get_max_area(array[i]))
    return result


if __name__ == '__main__':
    lst = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]
    ]
    mr_submatrix_area = maximum_rectangular_submatrix_area(lst)
    print(mr_submatrix_area)
