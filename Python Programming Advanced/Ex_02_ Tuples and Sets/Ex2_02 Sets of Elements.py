"""
Input	    Output
4 3         3
1           5
3
5
7
3
4
5

2 2         1
1
3
1
5
"""
set1 = set()
set2 = set()

n, m = (input().split(' '))
#Variant 2
#n, m - [int(x) for x in input().split()] - we took the "n" and "m" variables as integer

for i in range(int(n)+int(m)):
    number = (input())
    if i < int(n):
        set1.add(number)
    else:
        set2.add(number)

print('\n'.join(set1&set2))