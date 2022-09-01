"""
Input	                Output                                                  Comments
Tom, Jerry              Tom hits a wall and needs to rest.                      First is Tom. He moves to position (3, 2). He hits a wall and needs to rest.
. . T . . .             Jerry is out of the game! The winner is Tom.            Next is Jerry. He moves to position (1, 3). It is an empty position.
. . . . . .                                                                     Tom's next move (5, 1) is ignored because he is resting.
. . W . . .                                                                     Jerry moves to (5, 1). There is a trap, so he is out of the game. The program ends.
. . W . . E
. . . . . .
. T . W . .
(3, 2)
(1, 3)
(5, 1)
(5, 1)

Jerry, Tom              Jerry found the Exit and wins the game!
. T . . . W
. . . . T .
. W . . . T
. T . E . .
. . . . . T
. . T . . .
(1, 1)
(3, 0)
(3, 3)

Jerry, Tom              Jerry hits a wall and needs to rest.
. . . W . .             Tom hits a wall and needs to rest.
. . T T . .             Tom hits a wall and needs to rest.
. . . . . .             Jerry hits a wall and needs to rest.
. T . W . .             Tom found the Exit and wins the game!
W . . . E .
. . . W . .
(0, 3)
(3, 3)
(1, 3)
(2, 2)
(3, 5)
(4, 0)
(5, 3)
(3, 1)
(4, 4)
(4, 4)
"""
maze_board = []

current_player, other_player = input().split(", ")

ROWS_COUNT = 6
COLUMN_COUNTS = 6

for _ in range(ROWS_COUNT):
    row_elements = list(input().split())
    maze_board.append(row_elements)

have_winner = False
current_player_rest = False
other_player_rest = False

while True:
    row, col = eval(input())
    if not current_player_rest:
        player_step = maze_board[row][col]
        if player_step == "E":
            print(f"{current_player} found the Exit and wins the game!")
            have_winner = True
            break
        elif player_step == "T":
            print(f"{current_player} is out of the game! The winner is {other_player}.")
            have_winner = True
            break
        elif player_step == "W":
            print(f"{current_player} hits a wall and needs to rest.")
            current_player_rest = True
    else:
        current_player_rest = False

    if have_winner:
        break

    current_player, other_player = other_player, current_player
    current_player_rest, other_player_rest = other_player_rest, current_player_rest
