"""
Input	                Output
2 3                     5 2 3
1 2 3                   4 1 6
4 5 6                   Invalid input!
swap 0 0 1 1            5 4 3
swap 10 9 8 7           2 1 6
swap 0 1 1 0
END

1 2                     Invalid input!
Hello World             World Hello
0 0 0 1                 Hello World
swap 0 0 0 1
swap 0 1 0 0
END
"""
def is_outside(row,col,rows,cols):
    return row < 0 or col < 0 or row >= rows or col >= cols

rows, columns = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

command = input().split()

while command[0] != "END":
    if command[0] == "swap" and len(command) == 5:
#        row1 = command[1]
#        col1 = command[2]
#        row2 = command[3]
#        col2 = command[4]
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if is_outside(row1, col1, rows, columns) or is_outside(row2, col2, rows, columns):
            print("Invalid input!")
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                print(' '.join([str(x) for x in row]))
    else:
        print("Invalid input!")
    command = input().split()