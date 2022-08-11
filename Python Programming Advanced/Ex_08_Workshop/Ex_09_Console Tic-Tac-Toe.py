"""
Simple two-player tic-tac-toe game.
| X |   |   |           | 1 | 2 | 3 |
| O | X |   |           | 4 | 5 | 6 |
| O |   | X |           | 7 | 8 | 9 |
X - wins
"""
def build_initial_field(rows_count, columns_count):
    return [[None] * columns_count for _ in range(rows_count)]

def get_cell_value(cell):
    return cell if cell else " "

def print_field(field):
    new_field = [[get_cell_value(x) for x in row] for row in field]
    for row in new_field:
        print('|' + '|'.join([str(x) for x in row]) + '|')

def print_field_numeratino(first_player):
    field = [[1,2,3],[4,5,6],[7,8,9]]
    print("This is the numeration of the board: ")
    for row in field:
        print('|' + '|'.join([str(x) for x in row]) + '|')
    print(f"{first_player} start first!")

def print_winner(player):
    print(f'{player} wins!')

def player_initilize(player_one_name, player_two_name):
    players_dict = {}
    while True:
        player_one_symbol = input(f'{player_one_name} would you like to play with "X" or "O"? ')
        if player_one_symbol == "X":
            players_dict[player_one_name] = player_one_symbol
            players_dict[player_two_name] = "O"
            break
        elif player_one_symbol == "O":
            players_dict[player_one_name] = player_one_symbol
            players_dict[player_two_name] = "X"
            break
        else:
            print('The symbol must be "X" or "O" ')

    return players_dict

def apply_player_move(player_dict, current_player, field, free_indices):
    while True:
        player_move = int(input(f'{current_player} choose a free position [1-9]: '))
        if player_move in free_indices:
            row, column = field_updateing(player_move)
            free_indices.remove(player_move)
            field[row][column] = player_dict[current_player]
            break
        else:
            print("This position is already taken. Choose another one:")

    return field, free_indices

def field_updateing(move):
    positions = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }
    return positions[move]

def is_win_condition(field):
    if field[0][0] == field[0][1] == field[0][2] and field[0][0] != None or \
        field[1][0] == field[1][1] == field[1][2] and field[1][0] != None or \
        field[2][0] == field[2][1] == field[2][2] and field[2][0] != None or \
        field[0][0] == field[1][0] == field[2][0] and field[0][0] != None or \
        field[0][1] == field[1][1] == field[2][1] and field[1][1] != None or \
        field[0][2] == field[1][2] == field[2][2] and field[2][2] != None or \
        field[0][0] == field[1][1] == field[2][2] and field[0][0] != None or \
        field[2][0] == field[1][1] == field[0][2] and field[1][1] != None:
        return True

    else:

        return False

def play(field):
    player_dict = player_initilize(player_one_name, player_two_name)
    current_player, other_player = player_one_name, player_two_name
    print_field_numeratino(current_player)

    while True:
        apply_player_move(player_dict, current_player, field, free_indices)
        print_field(field)
        if is_win_condition(field):
            break
        else:
            current_player, other_player = other_player, current_player
    print_winner(current_player)

field = build_initial_field(3, 3)
free_indices = {1, 2, 3, 4, 5, 6, 7, 8, 9}

player_one_name = input(f'Player one name: ')
player_two_name = input(f'Player one name: ')

play(field)