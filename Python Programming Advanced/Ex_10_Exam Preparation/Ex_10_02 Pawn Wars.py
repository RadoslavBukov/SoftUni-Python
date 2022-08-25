"""
Input	                Output	                                                        Comments
- - - - - - b -         Game over! White pawn is promoted to a queen at b8.             We start by pushing the white pawn to b4, next, we push the black pawn to g7:
- - - - - - - -                                                                         - - - - - - - -
- - - - - - - -                                                                         - - - - - - b -
- - - - - - - -                                                                         - - - - - - - -
- - - - - - - -                                                                         - - - - - - - -
- w - - - - - -                                                                         - w - - - - - -
- - - - - - - -                                                                         - - - - - - - -
- - - - - - - -	                                                                        - - - - - - - -
                                                                                        - - - - - - - -
                                                                                        Then white play b5, black play g6:
                                                                                        - - - - - - - -
                                                                                        - - - - - - - -
                                                                                        - - - - - - b -
                                                                                        - w - - - - - -
                                                                                        - - - - - - - -
                                                                                        - - - - - - - -
                                                                                        - - - - - - - -
                                                                                        - - - - - - - -
                                                                                        …
                                                                                        Capturing is not possible here, so after a few more moves,
                                                                                        the white pawn is promoted to a queen on b8.


- - - - - - - -         Game over! White win, capture on a3.                            A white pawn always start first, so it must capture the black
- - - - - - - -                                                                         one on a3 in the first move:
- - - - - - - -                                                                         - - - - - - - -
- - - - - - - -                                                                         - - - - - - - -
- - - - - - - -                                                                         - - - - - - - -
b - - - - - - -                                                                         - - - - - - - -
- w - - - - - -                                                                         w - - - - - - -
- - - - - - - -	                                                                        - - - - - - - -
                                                                                        - - - - - - - -
"""
def possible_moves(player_position,delta, board):
    row, col = player_position
    possible_move = [
        [row+delta, col],
        [row+delta, col-1],
        [row+delta, col+1]
    ]
    result = []
    for possible_row, possible_col in possible_move:
        if possible_row >= 0 and possible_col >= 0 and possible_row < len(board) and possible_col < len(board):
            result.append(([possible_row, possible_col]))
    return result


def get_square_position(row, column):
      row_names = [8, 7, 6, 5, 4, 3, 2, 1]
      columns_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
      return f"{columns_names[column]}{row_names[row]}"

board = []

ROWS_COUNT = 8
COLUMN_COUNTS = 8

for row in range(ROWS_COUNT):
    row_elements = list(input().split())
    for col in range(COLUMN_COUNTS):
        if row_elements[col] == "w":
            white_row, white_col = row, col
        elif row_elements[col] == "b":
            black_row, black_col = row, col
    board.append(row_elements)

current_player = "w"
other_player = "b"
current_delta = -1
other_delta = +1
current_player_position = white_row, white_col
other_player_position = black_row, black_col
is_captured = False
is_queen = False

while True:
    moves = possible_moves(current_player_position, current_delta, board)
    player = "White" if current_player == "w" else "Black"
    for row, col in moves:
        if board[row][col] == other_player:
            is_captured = True
            break
        elif row in (0, ROWS_COUNT-1):
            is_queen = True
            break

    if is_captured or is_queen:
        break

    rows, cols = current_player_position
    board[rows][cols] = "-"
    board[rows+current_delta][cols] = current_player
    current_player_position = rows + current_delta, cols

    current_player, other_player = other_player, current_player
    current_delta, other_delta = other_delta, current_delta
    current_player_position, other_player_position = other_player_position, current_player_position
#    for _ in board:
#        print(" ".join(str(x) for x in _))

if is_captured:
    print(f"Game over! {player} win, capture on {get_square_position(row, col)}.")
elif is_queen:
    print(f"Game over! {player} pawn is promoted to a queen at {get_square_position(row, col)}.")