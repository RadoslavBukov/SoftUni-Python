"""
Input	    Output
2           6
7

10          50
50

37          185
200
"""

divisor = int(input())
boundary = int(input())
N = 0

for i in range(boundary+1, 0, -1):
    if i % divisor == 0 :
        N = i;
        break
print(N)
