"""
Test Code	                                    Output

@tags('p')                                      <p>Hello you!</p>
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')                                     <h1>HELLO</h1>
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
"""
from functools import wraps

def tags(params):
    def dec(func):

        @wraps(func)
        def wrapper(*args):
            return f"<{params}>{func(*args)}</{params}>"

        return wrapper
    return dec


# Test Code 1
@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

# Test Code 2
@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
