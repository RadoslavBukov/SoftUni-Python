"""
Test Code	                                                Output

@exec_time                                                  0.8342537879943848
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))

@exec_time                                                  0.14537858963012695
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))

@exec_time                                                  0.4199554920196533
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())
"""
from time import time
from functools import wraps


def exec_time(func):

    @wraps(func)
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()
        return end - start

    return wrapper


# Test Code 1
@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))

# Test Code 2
@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))

# Test Code 3
@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())