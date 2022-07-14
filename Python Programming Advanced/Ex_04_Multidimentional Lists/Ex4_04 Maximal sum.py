"""
Input	                Output
4 5                     Sum = 75
1 5 5 2 4               1 4 14
2 1 4 14 3              7 11 2
3 7 11 2 8              8 12 16
4 8 12 16 4

5 6                     Sum = 34
1 0 4 3 1 1             2 5 6
1 3 1 3 0 4             5 4 1
6 4 1 2 5 6             6 0 5
2 2 1 5 4 1
3 3 3 6 0 5
"""
rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = float("-inf")
start_row = 0
start_col = 0

for row in range(rows-2):
    for col in range(cols-2):
        sum = matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] + \
              matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] + \
              matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]
        if sum > max_sum:
            max_sum = sum
            start_row = row
            start_col = col

matrix_3 = []

for r in range(start_row, start_row+3):
    ll = []
    for c in range(start_col, start_col+3):
        ll.append(matrix[r][c])
    matrix_3.append(ll)

print(f"Sum = {max_sum}")
for rows2 in range(len(matrix_3)):
    print(f"{' '.join([str(x) for x in matrix_3[rows2]])}")