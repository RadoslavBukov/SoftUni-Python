"""
Input	                Output
6, 5                    You've collected:
. . . . .               - 2 Christmas decorations
C . . G .               - 1 Gifts
. C . . .               - 0 Cookies
G . . C .               . . . . .
. D . . D               C . . G .
Y . . . G               . C . . .
left-3                  G . Y C .
up-1                    x x x x x
left-2                  x . x x x
right-7
up-1
End

5, 6                    Merry Christmas!
. . . . . .             You've collected:
. . . . . .             - 2 Christmas decorations
Y C D D . .             - 0 Gifts
. . . C . .             - 3 Cookies
. . . C . .             . . . . . .
right-3                 . . . . . .
down-3	                x x x x . .
                        . . . x . .
                        . . . Y . .

5, 2                    You've collected:
. .                     - 0 Christmas decorations
. .                     - 0 Gifts
. Y                     - 0 Cookies
. .                     x .
. G                     Y x
up-1                    x x
left-11                 x .
down-10                 x G
End
"""
def is_out(row, col, rows_count, cols_count):
    if row >= rows_count:
        row = 0
    if col >= cols_count:
        col = 0
    if row < 0:
        row = rows_count - 1
    if col < 0:
        col = cols_count - 1

    return row, col

def matrix_collect_elements(mm):
    items = ["D", "G", "C"]
    for row in mm:
        for column in row:
            if column in items:
                return False
    return True

santa_shop = []
rows_count, cols_count = [int(x) for x in input().split(", ")]

for row in range(rows_count):
    row_elements = list(input().split())
    for col in range(cols_count):
        if row_elements[col] == "Y":
            current_row, current_col = row, col

    santa_shop.append(row_elements)

directions = {
    'right': lambda r, c: (r, c+1),
    'left': lambda r, c: (r, c-1),
    'up': lambda r, c: (r-1, c),
    'down': lambda r, c: (r+1, c),
}

christmas_decoration = 0
gifts = 0
cookies = 0
all_items_collected = False

commands = input().split("-")

while commands[0] != "End":
    direction = commands[0]
    steps = int(commands[1])

    for _ in range(steps):
        santa_shop[current_row][current_col] = 'x'
        row, col = directions[direction](current_row, current_col)
        row, col = is_out(row, col, rows_count, cols_count)

        if santa_shop[row][col] == "D":
            christmas_decoration += 1
        elif santa_shop[row][col] == "G":
            gifts += 1
        elif santa_shop[row][col] == "C":
            cookies += 1

        santa_shop[row][col] = "Y"
        current_row, current_col = row, col

        if matrix_collect_elements(santa_shop):
            print("Merry Christmas!")
            all_items_collected = True
            break

    if all_items_collected:
        break

    commands = input().split("-")


print("You've collected:")
print(f"- {christmas_decoration} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for _ in santa_shop:
    print(" ".join(str(x) for x in _))