"""
Test Code	                            Output

generator = fibonacci()                 0
for i in range(5):                      1
    print(next(generator))              1
                                        2
                                        3

generator = fibonacci()                 0
for i in range(1):
    print(next(generator))
"""
def fibonacci():
    first = 0
    second = 1

    yield first
    yield second

    while True:
        result = first+second
        first, second = second, result
        yield result

# Test Code 1
generator = fibonacci()
for i in range(5):
    print(next(generator))

# Test Code 2
# generator = fibonacci()
# for i in range(1):
#     print(next(generator))
