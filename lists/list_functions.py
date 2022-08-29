'''
    Module File for list functions
'''


def reverse(list1):
    '''
        Function to Reverse a list
            list1 = list1[::-1]                                        # Using negative indexing
                or
            list1 = list(reversed(list1))                              # Using reversed function
                or
            list1.reverse()                                            # Using reverse method
                or
            list1 = [list1[len(list1)-1-i] for i in range(len(list1))] # Using Comprehension
    '''
    new_list = []
    llen = list_length(list1)
    for i in range(llen):
        new_list.append(list1[llen - 1 - i])
    return new_list


def swap_elements(list1, position1, position2):
    '''
        Function to swap elements at position1 and position2 in a list
            Simple Way:
                list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
    '''
    temp = list1[position1]
    list1[position1] = list1[position2]
    list1[position2] = temp
    return list1


def numbers_square(list1):
    '''
        Program to create a list of square of numbers
    '''
    return list(map(lambda x: (x, x ** 2), list1))


def numbers_cube(list1):
    '''
        Program to create a list of cube of numbers
    '''
    return list(map(lambda x: (x, x ** 3), list1))


def remove_nth_occurrence_from_list(list1, element, n=1):
    '''
        Program to remove nth occurrence of element from a list
    '''
    count = 0
    for idx, ele in enumerate(list1):
        if ele == element:
            count += 1

        if count == n:
            list1.pop(idx)
            break
    return list1


def list_length(list1):
    '''
        Program to get length of a array
            return len(arr)             # Using len function
                or 
            return arr.__len__()        # Using list magic method
    '''
    count = 0
    for _ in list1:
        count += 1
    return count


def is_element_in_list(list1, element):
    '''
        Program to check if element exists in list
            return element in list1                                   # Using in Operator
                or
            return bool([ele for ele in list1 if ele == element])     # Using Comprehension
                or
            return bool(list1.count(element))                         # Using count method
                or
            return any(ele for ele in list1 if ele == element)        # Using any function
    '''
    for ele in list1:
        if ele == element:
            return True
    return False


if __name__ == '__main__':
    lst = [6, 9, 3, 7, 1, 2, 8]
    print(reverse(lst))
    print(swap_elements(lst, 0, 4))
    lst = [1, 2, 3, 4]
    print(numbers_square(lst))
    print(numbers_cube(lst))
    lst = ['python', 'is', 'easy', 'is', 'english', 'is', 'best']
    print(list_length(lst))
    print(remove_nth_occurrence_from_list(lst, 'is', n=2))
    print(list_length(lst))
    print(is_element_in_list(lst, 'easy'))
    print(is_element_in_list(lst, 'Easy'))
