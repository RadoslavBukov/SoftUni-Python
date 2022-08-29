"""
Input	                                                    Output
- R - - - -                                                 Water deposit found at (3, 1)
- - - - - R                                                 Concrete deposit found at (4, 3)
- E - R - -                                                 Metal deposit found at (5, 0)
- W - - - -                                                 Area suitable to start the colony.
- - - C - -
M - - - - -
down, right, down, right, down, left, left, left

R - - - - -                                                 Water deposit found at (3, 2)
- - C - - -                                                 Water deposit found at (4, 3)
- - - - M -                                                 Rover got broken at (4, 5)
- - W - - -                                                 Area not suitable to start the colony.
- E - W - R
- - - - - -
up, right, down, right, right, right

R - - - - -                                                 Water deposit found at (4, 3)
- - C - - -                                                 Metal deposit found at (3, 2)
- - - - M -                                                 Concrete deposit found at (3, 0)
C - M - R M                                                 Metal deposit found at (3, 5)
- E - W - -                                                 Rover got broken at (3, 4)
- - - - - -                                                 Area suitable to start the colony.
right, right, up, left, left, left, left, left
"""
def is_out(row, col, field):
    if row >= len(field):
        row = 0
    if col >= len(field):
        col = 0
    if row < 0:
        row = len(field) - 1
    if col < 0:
        col = len(field) - 1

    return row, col

field = []

ROWS_COUNT = 6
COLUMN_COUNTS = 6

for row in range(ROWS_COUNT):
    row_elements = list(input().split())
    for col in range(COLUMN_COUNTS):
        if row_elements[col] == "E":
            rover_row, rover_col = row, col

    field.append(row_elements)

directions = {
    'right': lambda r, c: (r, c+1),
    'left': lambda r, c: (r, c-1),
    'up': lambda r, c: (r-1, c),
    'down': lambda r, c: (r+1, c),
}

commands = input().split(", ")
water = False
concrete = False
metal = False

for command in commands:
    field[rover_row][rover_col] = '-'
    row, col = directions[command](rover_row, rover_col)
    row, col = is_out(row, col, field)

    if field[row][col] == "W":
        water = True
        print(f"Water deposit found at ({row}, {col})")
    elif field[row][col] == "M":
        metal = True
        print(f"Metal deposit found at ({row}, {col})")
    elif field[row][col] == "C":
        concrete = True
        print(f"Concrete deposit found at ({row}, {col})")
    elif field[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

    field[row][col] = "E"
    rover_row, rover_col = row, col

if water and concrete and metal:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")