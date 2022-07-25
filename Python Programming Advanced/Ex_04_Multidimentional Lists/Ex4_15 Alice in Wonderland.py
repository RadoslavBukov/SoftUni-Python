"""
Input	                Output
5                       Alice didn't make it to the tea party.
. A . . 1               . * . . 1
R . 2 . .               * * * . .
4 7 . 1 .               4 * . 1 .
. . . 2 .               . . . 2 .
. 3 . . .               . 3 . . .
down
right
left
down
up
left

7                       She did it! She went to the party.
. A . 1 1 . .           * * . 1 1 . .
9 . . . 6 . 5           * . . . 6 . 5
. 6 . R . . .           * * . R . . .
. 3 . . 1 . .           . 3 . . 1 . .
. . . 2 . . 2           . . . 2 . . 2
. 3 . . 1 . .           . 3 . . 1 . .
. 8 3 . . . 2           . 8 3 . . . 2
left
down
down
right
"""
def moveing(row, col, matrix):
    tea = 0
    moveing.end = False
    if row < len(matrix) and col < len(matrix):
        if matrix[row][col].isdigit():
            tea += int(matrix[row][col])
            matrix[row][col] = '*'
        elif matrix[row][col] == "R":
            print("Alice didn't make it to the tea party.")
            matrix[row][col] = '*'
            for rows in matrix:
                print(*rows)
            moveing.end = True

        else:
            matrix[row][col] = '*'
    else:
        print("Alice didn't make it to the tea party.")
        for rows in matrix:
            print(*rows)
        moveing.end = True

    return tea

size = int(input())
matrix = []

alice_row = 0
alice_col = 0

for row in range(size):
    row_elements = (input().split())
    for col in range(size):
        if row_elements[col] == "A":
                alice_row = row
                alice_col = col
    matrix.append(row_elements)

directions = {
    'right': lambda r, c: (r, c+1),
    'left': lambda r, c: (r, c-1),
    'up': lambda r, c: (r-1, c),
    'down': lambda r, c: (r+1, c),
}
tea_collect = 0
move = input()
end = False

while not end:
    matrix[alice_row][alice_col] = '*'
    row, col = directions[move](alice_row, alice_col)
    alice_row = row
    alice_col = col
    tea_collect += int(moveing(row, col, matrix))
    if tea_collect >= 10:
        print("She did it! She went to the party.")
        matrix[row][col] = '*'
        for rows in matrix:
            print(*rows)
        break
    end = moveing.end
    if end:
        break
    move = input()
