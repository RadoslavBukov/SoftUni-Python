"""
Input	        Output
5               1
0K0K0
K000K
00K00
K000K
0K0K0

2               0
KK
KK

8               12
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK
"""
def possible_move(row, col, size):
    possible_moves = [
        [row-2, col+1],
        [row-1, col+2],
        [row+1, col+2],
        [row+2, col+1],
        [row+2, col-1],
        [row+1, col-2],
        [row-1, col-2],
        [row-2, col-1]
    ]
    result = []
    for possible_row, possible_col in possible_moves:
        if possible_row >= 0 and possible_col >= 0 and possible_row < size and possible_col < size:
            result.append(([possible_row, possible_col]))
    return result

def agressive_horse(matrix):
    knight_attacks = 0
    knight_max_attack = float("-inf")
    knight_max_attack_row = 0
    knight_max_attack_col = 0

    for row_idx in range(len(matrix)):
        for col_idx in range(len(board[row_idx])):
            if board[row_idx][col_idx] == "K":
                knight_attacks = 0
                for move_row, move_col in possible_move(row_idx, col_idx, size):
                    if board[move_row][move_col] == "K":
                        knight_attacks += 1
                if knight_attacks > knight_max_attack:
                    knight_max_attack = knight_attacks
                    knight_max_attack_row = row_idx
                    knight_max_attack_col = col_idx

    if knight_max_attack > 0:
        return knight_max_attack_row, knight_max_attack_col
    else:
        return None

size = int(input())

board = []

for _ in range(size):
    board.append([x for x in input()])

removed = 0

while agressive_horse(board) != None:
    next_row, next_col = agressive_horse(board)
    board[next_row][next_col] = "O"
    removed += 1

print(removed)