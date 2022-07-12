cube=[
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ],
    [
        [9, 10],
        [11, 12]
    ],
]
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

# Print the row in matrix:
#[1, 2, 3]
#[4, 5, 6]
#[7, 8, 9]
def cube_rows(cb):

    for mm_idx in range(len(cb)):
        for row_idx in range(len(cb[mm_idx])):
            print(f"Matrix row: {row_idx} {cb[mm_idx][row_idx]}")

    for mm in cb:
        for row in mm:
            print(f"Matrix row: {row}")

#cube_rows(cube)
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

# Print the colums in matrix:
# 1, 4, 7
# 2, 5, 8
# 3, 6, 9
def cube_columns(cb):
    for row in range(len(cb)):
        row += 2
    print(cb)

#cube_columns(cube)
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

# Print all elements in matrix and its sum:
def cube_elements(cb):
    print("All elements by elements:")
    sum = 0
    sum2 = 0
    for mm in cb:
        for row in mm:
            for column in row:
                print(column, end=" ")
                sum += column
    print(f"\nSum = {sum}")

    print("\nAll elements by index:")
    for mm_idx in range(len(cb)):
        for row_idx in range(len(cb[mm_idx])):
            for column_idx in range(len(cb[mm_idx][row_idx])):
                print(cb[mm_idx][row_idx][column_idx], end=" ")
                sum2 += cb[mm_idx][row_idx][column_idx]
    print(f"\nSum = {sum2}")

#cube_elements(cube)

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
# Print all elements in new list:
def flattering_cube(cb):
    print("All elements by elements:")
    list_matrix = []
    for mm in cb:
        for row in mm:
            for column in row:
                list_matrix.append(column)
    print(list_matrix, end=" ")

    print("\nAll elements by index:")
    list_matrix2 = []

    for mm_idx in range(len(cb)):
        for row_idx in range(len(cb[mm_idx])):
            for column_idx in range(len(cb[mm_idx][row_idx])):
                list_matrix2.append(cb[mm_idx][row_idx][column_idx])
    print(list_matrix2, end=" ")

flattering_cube(cube)