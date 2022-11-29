"""
Test Code	                                        Output

@type_check(int)                                    4
def times2(num):                                    Bad Type
    return num*2
print(times2(2))
print(times2('Not A Number'))

@type_check(str)                                    H
def first_letter(word):                             Bad Type
    return word[0]
print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
"""
from functools import wraps

def type_check(params):
    def dec(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, params):
                    return func(*args, **kwargs)
                return "Bad Type"

        return wrapper
    return dec


# Test Code 1
@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

# Test Code 2
@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
