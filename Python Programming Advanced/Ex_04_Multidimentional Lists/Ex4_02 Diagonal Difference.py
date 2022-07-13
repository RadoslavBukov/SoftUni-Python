"""
Input	            Output	        Comments
3                   15              Primary diagonal: sum = 11 + 5 + (-12) = 4
11 2 4                              Secondary diagonal: sum = 4 + 5 + 10 = 19
4 5 6                               Difference: |4 - 19| = 15
10 8 -12

4                   34
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14
"""
n = int(input())
matrix = []
primary_sum = 0
secondary_sum = 0

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

for idx in range(n):
    primary_sum += matrix[idx][idx]
    secondary_sum += matrix[idx][n-idx-1]

print(abs(primary_sum-secondary_sum))