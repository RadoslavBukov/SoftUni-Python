"""
Input	        Output
2               [2, 4, 6, 8, 10]
5

1               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
10
"""

factor = int(input())
count = int(input())
list=[]

for i in range(factor, count*factor+1, factor):
    list.append((i))
print(list)
