'''
    Program to print different star (*) patterns
'''


def star_pattern(rows):
    '''
        Function to Print Bottom Left Triangle
            *
            **
            ***
            ****
            *****
    '''
    for i in range(rows):
        print('*'*(i+1))


def star_pattern_rjust(rows):
    '''
        Function to Print Bottom Right Triangle
                *
               **
              ***
             ****
            *****
    '''
    for i in range(rows):
        print(('*'*(i+1)).rjust(rows))


def inverted_star_pattern(rows):
    '''
        Function to Print Top Left Triangle
            *****
            ****
            ***
            **
            *
    '''
    for i in range(rows):
        print('*'*(rows-i))


def inverted_star_pattern_rjust(rows):
    '''
        Function to Print Top Right Triangle
            *****
             ****
              ***
               **
                *
    '''
    for i in range(rows):
        print(('*'*(rows-i)).rjust(rows))


def star_pattern_block(rows):
    '''
        Function to Print a Block enclosed by Top/Bottom Left/Right Triangles
            **********
            ****  ****
            ***    ***
            **      **
            *        *
            *        *
            **      **
            ***    ***
            ****  ****
            **********
    '''
    for i in range(rows):
        print(('*'*(rows-i)).ljust(rows) + ('*'*(rows-i)).rjust(rows))
    for i in range(rows):
        print(('*'*(i+1)).ljust(rows) + ('*'*(i+1)).rjust(rows))


if __name__ == '__main__':
    star_pattern(5)
    star_pattern_rjust(5)
    inverted_star_pattern(5)
    inverted_star_pattern_rjust(5)
    star_pattern_block(5)
