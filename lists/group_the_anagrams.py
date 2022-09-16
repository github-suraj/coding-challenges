'''
    Write a program to Group the anagrams together.
    input = [
        "CARS", "REPAID", "DUES", "NOSE", "SIGNED", "LANE", "PAIRED", "ARCS",
        "GRAB", "USED", "ONES", "BRAG", "SUED", "LEAN", "SCAR", "DESIGN"
    ]
    Output:
        CARS ARCS SCAR
        REPAID PAIRED
        DUES USED SUED
        NOSE ONES
        SIGNED DESIGN
        LANE LEAN
        GRAB BRAG
'''

def group_anagrams(words):
    '''
        Function to Group the anagrams together
    '''
    output = []
    while words:
        start = words.pop(0)
        output.append([start])
        for i, word in enumerate(words):
            if len(word) == len(start) and set(word) == set(start):
                output[-1].append(words.pop(i))
    return output


if __name__ == '__main__':
    lst = [
        "CARS", "REPAID", "DUES", "NOSE", "SIGNED", "LANE", "PAIRED", "ARCS",
        "GRAB", "USED", "ONES", "BRAG", "SUED", "LEAN", "SCAR", "DESIGN"
    ]
    groups = group_anagrams(lst)
    for group in groups:
        print(' '.join(group))
