"""
Input                   Output
1 2 3 4 5               5 4 3 2 1

1                       1
"""
s = input().split()

while s:
    print(s.pop(), end=' ')
