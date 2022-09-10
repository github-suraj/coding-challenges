'''
    Given a binary matrix,
        find out the maximum size square sub-matrix with all 1s.
        For example, consider the below binary matrix.
            +---+---+---+---+---+
            | 0 | 1 | 1 | 0 | 1 |
            +---+---+---+---+---+
            | 1 | 1 | 0 | 1 | 0 |
            +---+---+---+---+---+
            | 0 | 1 | 1 | 1 | 0 |
            +---+---+---+---+---+
            | 1 | 1 | 1 | 1 | 0 |
            +---+---+---+---+---+
            | 1 | 1 | 1 | 1 | 1 |
            +---+---+---+---+---+
            | 0 | 0 | 0 | 0 | 0 |
            +---+---+---+---+---+
        Output:
            +---+---+---+
            | 1 | 1 | 1 |    # Row 2 Coulumn 1-2-3
            +---+---+---+
            | 1 | 1 | 1 |    # Row 3 Coulumn 1-2-3
            +---+---+---+
            | 1 | 1 | 1 |    # Row 4 Coulumn 1-2-3
            +---+---+---+
'''

def maximum_square_submatrix(array):
    '''
        Function to find maximum square submatrix with all 1's
    '''
    rows = len(array)
    columns = len(array[0])
    max_count = 0

    sub_array = [[0 for _ in range(columns)] for _ in range(2)]
    for i in range(rows):
        for j in range(columns):
            entry = array[i][j]
            if entry and j:
                entry = 1 + min(sub_array[1][j-1],
                                min(sub_array[0][j-1], sub_array[1][j])
                            )
            sub_array[0][j], sub_array[1][j] = sub_array[1][j], entry
            max_count = max(max_count, entry)

    return [[1 for _ in range(max_count)] for _ in range(max_count)]


if __name__ == '__main__':
    lst = [
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    ms_submatrix = maximum_square_submatrix(lst)
    print(ms_submatrix)
