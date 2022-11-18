"""
Test Code	                                                                            Output

for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):                string2dict
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):                                     N
    print(i)                                                                            e
                                                                                        e
                                                                                        d
                                                                                        2
                                                                                        3
                                                                                        words
                                                                                        .
"""
def read_next(*args):
    for item in args:
        for el in item:
            yield el

# Test Code 1
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

# Test Code 2
# for i in read_next("Need", (2, 3), ["words", "."]):
#     print(i)
