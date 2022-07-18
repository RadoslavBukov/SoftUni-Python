"""
Input	                Output
3                       6 2 3
1 2 3                   4 3 6
4 5 6                   7 8 9
7 8 9
Add 0 0 5
Subtract 1 1 2
END

4                       Invalid coordinates
1 2 3 4                 Invalid coordinates
5 6 7 8                 -41 2 3 4
8 7 6 5                 5 6 7 8
4 3 2 1                 8 7 6 5
Add 4 4 100             4 3 2 101
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END
"""
def is_valid(row, col, size):
    return row >= 0 and col >= 0 and row < size and col < size

size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

command = input().split()

while command[0] != "END":
    action = command[0]
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if not is_valid(row, col, size):
        print("Invalid coordinates")
        command = input().split()
        continue
    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value
    command = input().split()

for rows in matrix:
    print(*rows)