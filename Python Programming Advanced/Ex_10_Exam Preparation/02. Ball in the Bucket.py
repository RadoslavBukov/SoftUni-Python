"""
Input	                    Output
10 30 B 4 20 24             Sorry! You need 33 points more to win a prize.
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)

B 30 14 23 20 24            Good job! You scored 299 points, and you've won Teddy Bear.
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)
"""
def matrix_columns(col, mm):
    sum = 0

    for row_index in range(len(mm)):
        if mm[row_index][col].isdigit():
            sum += int(mm[row_index][col])
    return sum

def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size

board = []

ROWS_COUNT = 6
COLUMN_COUNTS = 6

for _ in range(ROWS_COUNT):
    row_elements = list(input().split())
    board.append(row_elements)

score = 0

for throw in range(3):
    row, col = eval(input())

    if is_inside(row, col, len(board)):
        hit = board[row][col]
    else:
        continue

    # if hit.isdigit():
    #     score += int(hit)
    if hit == "B":
        score += matrix_columns(col, board)
        board[row][col] = "x"

prize = ""

if 100 <= score <= 199:
    prize = "Football"
elif 200 <= score <= 299:
    prize = "Teddy Bear"
if 300 <= score:
    prize = "Lego Construction Set"

if prize != "":
    print(f"Good job! You scored {score} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100-score} points more to win a prize.")

