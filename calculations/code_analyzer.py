'''
    Write code that can analyze code submissions.
    Write a function named 'validate' that takes
        code represented as a string as its only parameter.
    Your function should check a few things:
        the code must contain the def keyword
            otherwise return "missing def"
        the code must contain the : symbol
            otherwise return "missing :"
        the code must contain ( and ) for the parameter list
            otherwise return "missing paren"
        the code must not contain ()
            otherwise return "missing param"
        the code must contain four spaces for indentation
            otherwise return "missing indent"
        the code must contain validate
            otherwise return "wrong name"
        the code must contain a return statement
            otherwise return "missing return"
        If all these conditions are satisfied, your code should return True.

    Here comes the twist:
        your solution must return True when validating itself.
'''

import inspect
from xmlrpc.client import boolean

def validate(code, result=True):
    '''
        Basic function to analyze code submissions
    '''
    if 'def' not in code:
        result = "missing def"
    if ':' not in code and isinstance(result, boolean):
        result = "missing :"
    if '(' not in code or ')' not in code and isinstance(result, boolean):
        result = "missing paren"
    if '(' + ')' in code and isinstance(result, boolean):
        result = "missing param"
    if '    ' not in code and isinstance(result, boolean):
        result = "missing indent"
    if 'validate' not in code and isinstance(result, boolean):
        result = "wrong name"
    if 'return' not in code and isinstance(result, boolean):
        result = "missing return"
    return result


if __name__ == '__main__':
    CODE = inspect.getsource(validate)
    print(validate(CODE))
