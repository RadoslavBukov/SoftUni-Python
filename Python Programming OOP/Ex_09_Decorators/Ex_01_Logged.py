"""
Test Code	                        Output

@logged                             you called func(4, 4, 4)
def func(*args):                    it returned 6
    return 3 + len(args)
print(func(4, 4, 4))

@logged                             you called sum_func(1, 4)
def sum_func(a, b):                 it returned 5
    return a + b
print(sum_func(1, 4))
"""
from functools import wraps

def logged(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"you called {func.__name__}{args}\nit returned {func(*args, **kwargs)}"

    return wrapper

# Test Code 1
@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

# Test Code 2
@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
