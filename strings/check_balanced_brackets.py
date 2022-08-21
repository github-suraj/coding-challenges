'''
Program to Check Balanced of Parenthesis
    string1 = '{}{[]}'
        output -> True
    string2 = '{Suraj}{[Jaiswal]}'
        output -> True
    string3 = '{Suraj[}]{Jaiswal}'
        output -> False
    string4 = '{[{]}}'
        output -> False
'''


def is_balanced_brackets(_string):
    '''
        Verify if string is having balanced open and closed brackets
    '''
    stack = []
    for char in _string:
        if char in ('(', '[', '{'):
            stack.append(char)
        elif char not in (')', ']', '}'):
            continue
        else:
            if not stack:
                return False
            
            last_char = stack.pop()
            if char == ')' and last_char != '(':
                return False
            if char == ']' and last_char != '[':
                return False
            if char == '}' and last_char != '{':
                return False
    
    if stack:
        return False

    return True


if __name__ == '__main__':
    print(is_balanced_brackets('{}{[]}'))
    print(is_balanced_brackets('{Suraj}{[Jaiswal]}'))
    print(is_balanced_brackets('{Suraj[}]{Jaiswal}'))
    print(is_balanced_brackets('{[{]}}'))
