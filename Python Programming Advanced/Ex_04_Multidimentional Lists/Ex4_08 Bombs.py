"""
Input	            Output	                    Comments
4                   Alive cells: 3              1) The bomb with value 7 will explode and reduce the values of the cells around it.
8 3 2 5             Sum: 12                     2) The bomb with coordinates 2,1 and value 9 will explode and reduce its neighbor cells.
6 4 7 9             8 -4 -5 -2                  3) The bomb with coordinates 2,0 and value 9 will explode.
9 9 3 6             -3 -3 0 2                   After that, you have to print the count of the alive cells - 3, and their sum - 12. Print the matrix after the explosions.
6 8 1 2             0 0 -4 -1
1,2 2,1 2,0	        -3 -1 -1 2

3                   Alive cells: 3
7 8 4               Sum: 8
3 1 5               4 1 0
6 4 9               0 -3 -8
0,2 1,0 2,2	        3 -8 0
"""
def get_children(matrix, row, col):
    possible_children = [
        [row-1,col-1],
        [row-1,col],
        [row-1,col+1],
        [row,col-1],
        [row,col+1],
        [row+1,col-1],
        [row+1,col],
        [row+1,col+1],
    ]
    result = []
    for child_row, child_col in possible_children:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row,child_col])
    return result

size = int(input())

matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(",")]
    power = matrix[row][col]
    if power <= 0:
        continue

    matrix[row][col] = 0

    children = get_children(matrix, row, col)
    for child_row, child_col in children:
        matrix[child_row][child_col] -= power

alive_cells_count = 0
alive_cells_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells_sum += el
            alive_cells_count += 1

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")
for row in matrix:
    print(*row, sep=" ")