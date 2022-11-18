"""
Test Code	                                                    Output

[print(n) for n in possible_permutations([1, 2, 3])]	        [1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]

[print(n) for n in possible_permutations([1])]	                [1]
"""
from itertools import permutations

def possible_permutations(elements):
    for result in permutations(elements):
        yield list(result)

# Test Code 1
[print(n) for n in possible_permutations([1, 2, 3])]

# Test Code 2
[print(n) for n in possible_permutations([1])]
