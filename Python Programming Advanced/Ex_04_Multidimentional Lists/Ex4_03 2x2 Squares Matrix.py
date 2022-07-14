"""
Input	    Output	    Comments
3 4         2           Two 2x2 squares of equal cells:
A B B D                 A "B B" D           A B B D
E B B B                 E "B B" B           E B "B B"
I J B B                 I J B B             I J "B B"

2 2         0
a b
c d

5 4         3
A A B D
A A B B
I J B B
C C C G
C C K P
"""
rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

squares = 0

for row in range(rows-1):
    for col in range(cols-1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            squares += 1

print(squares)