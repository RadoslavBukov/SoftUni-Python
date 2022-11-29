"""
Test Code	                                        Output
@make_bold                                          <b><i><u>Hello, Peter</u></i></b>
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"
print(greet("Peter"))

@make_bold                                          <b><i><u>Hello, Peter, George</u></i></b>
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"
print(greet_all("Peter", "George"))
"""
from functools import wraps

def make_bold(func):
    @wraps(func)
    def wrapper(*args):
        return f"<b>{func(*args)}</b>"
    return wrapper

def make_italic(func):
    @wraps(func)
    def wrapper(*args):
        return f"<i>{func(*args)}</i>"
    return wrapper

def make_underline(func):
    @wraps(func)
    def wrapper(*args):
        return f"<u>{func(*args)}</u>"
    return wrapper


# Test Code 1
@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"
print(greet("Peter"))


#Test Code 2
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"
print(greet_all("Peter", "George"))
