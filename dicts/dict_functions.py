'''
    Module File for dictionary functions
'''


def list_of_tuples_to_dict(list_of_tuples):
    '''
        Function to convert list of tuples to dictionay
            tuple should be of length 2
    '''
    dict1 = {}
    for value0, value1 in list_of_tuples:
        dict1[value0] = value1
    return dict1


def add_two_dictionaries(dict1, dict2):
    '''
        Function to add two dictionaries
    '''
    dict3 = {}
    for key, value in dict1.items():
        dict3[key] = value

    for key, value in dict2.items():
        dict3[key] = value

    return dict3


if __name__ == '__main__':
    d1 = {'A': 72, 'B': 27, 'C': 7, 'D': 53}
    d2 = {'C': 53, 'D': 42, 'E': 92, 'F': 94}
    list_of_tup = (('A', 72), ('B', 27), ('C', 7), ('D', 53))
    print(list_of_tuples_to_dict(list_of_tup))
    print(add_two_dictionaries(d1, d2))
