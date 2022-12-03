"""
Test Code	                        results.txt

@store_results                      Function 'add' was called. Result: 4
def add(a, b):                      Function 'mult' was called. Result: 24
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
"""
from functools import wraps

def store_results(func):

    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        with open("./result.txt", "a") as file:
            file.write(f"Function '{func.__name__}' was called. Result: {result}")
            file.write("\n")
        return result

    return wrapper


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

print(add(2, 2))
print(mult(6, 4))
