"""
Input	                        Output	                Comment
5                               right                   The number of eggs if the bunny goes up is equal to 7. If he goes down = 9, there are no eggs on the left and 87 on the right.
1 3 7 9 11                      [3, 1]                  That's why the bunny should follow this direction (right) and collect the eggs provided there.
X 5 4 X 63                      [3, 2]
7 3 21 95 1                     [3, 3]
B 1 73 4 9                      [3, 4]
9 2 33 2 0	                    87

8
4 18 9 7 24 41 52 11            down
54 21 19 X 6 34 75 57           [6, 2]
76 67 7 44 76 27 56 37          [7, 2]
92 35 25 37 52 34 56 72         113
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22
"""
def best_path(row, col, matrix):
    directions = ['up', 'right', 'down', 'left']
    total_eggs = 0
    max_eggs = float('-inf')
    best_direction = ''


    for direction in directions:
        total_eggs = 0
        last_path = []
        path = different_directions(direction, row, col, matrix)
        for row1, col1 in path:
            if matrix[row1][col1] == "X":
                break
            else:
                total_eggs += int(matrix[row1][col1])
                last_path.append([row1, col1])

        if total_eggs > max_eggs and path:
            best_path = []
            max_eggs = total_eggs
            best_direction = direction
            best_path = last_path

    print(best_direction)
    for elements in best_path:
         print(elements, end='\n')
    print(max_eggs)

def different_directions(direction, row, col, matrix):
    path = []
    if direction == "up":
        for row in range(row-1, -1, -1):
            path.append([row, col])
    elif direction == "right":
        for col in range(col+1, len(matrix)):
            path.append([row, col])
    elif direction == "down":
        for row in range(row+1, len(matrix)):
            path.append([row, col])
    elif direction == "left":
        for col in range(col-1, -1, -1):
            path.append([row, col])
    return path


size = int(input())
matrix = []

for _ in range(size):
    matrix.append(input().split())

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix[row_idx])):
        if matrix[row_idx][col_idx] == "B":
            bunny_row = row_idx
            bunny_col = col_idx

max_eggs = best_path(bunny_row, bunny_col, matrix)



