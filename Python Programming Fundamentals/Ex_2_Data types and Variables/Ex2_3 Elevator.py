"""
Input	    Output	             Comments
17          6                    5 courses * 3 people + 1 course * 2 persons
3

4                               All the persons fit inside the elevator. Only one course is needed.
5	        1

10          2                   2 courses * 5 people
5
"""

import math
N = int(input())
P = int(input())

print(math.ceil(N/P))