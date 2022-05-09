"""
Input	    Output              Input       Output
5           Before:             10          Before:
10          a = 5               20          a = 10
            b = 10                          b = 20
            After:                          After:
            a = 10                          a = 20
            b = 5                           b = 10
"""
a = int(input())
b = int(input())

print(f"Before: \na = {a} \nb = {b}")
c=a
a=b
b=c
print(f"After: \na = {a} \nb = {b}")