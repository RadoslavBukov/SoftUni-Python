"""
Test Code	                    Output

fibonacci(3)                    {1: 1, 0: 0, 2: 1, 3: 2}
print(fibonacci.log)

fibonacci(4)                    {1: 1, 0: 0, 2: 1, 3: 2, 4: 3}
print(fibonacci.log)
"""
from functools import wraps

def cache(func):
    log = {}

    @wraps(func)
    def wrapper(n):
        if n in log:
            return log[n]
        result = func(n)
        log[n] = result
        return result

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Test Code 1
fibonacci(3)
print(fibonacci.log)

# Test Code 2
fibonacci(4)
print(fibonacci.log)
