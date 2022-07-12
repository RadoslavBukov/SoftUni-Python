matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

# Print the row in matrix:
#[1, 2, 3]
#[4, 5, 6]
#[7, 8, 9]
def matrix_rows(mm):
    for row_idx in range(len(mm)):
        print(f"Matrix row: {row_idx} {mm[row_idx]}")

    for row in mm:
        print(f"Matrix row: {row}")

#matrix_rows(matrix)
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

# Print the columns in matrix:
# 1, 4, 7
# 2, 5, 8
# 3, 6, 9
def matrix_columns(mm):
    rows = 3
    columns = 3
    columns_list = [[],[],[]]
#    for row_index in range(rows):
#        for column_index in range(columns):
#            columns_list[column_index].append(mm[row_index][column_index])
#    print(columns_list)

    for row_index in range(rows):
        for column_index in range(columns):
            columns_list[column_index].append(mm[row_index][column_index])
    print(columns_list)

#matrix_columns(matrix)
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

# Print all elements in matrix and its sum:
def matrix_elements(mm):
    print("All elements by elements:")
    sum = 0
    sum2 = 0
    for row in mm:
        for column in row:
            print(column, end=" ")
            sum += column
    print(f"\nSum = {sum}")

    print("\nAll elements by index:")
    for row_idx in range(len(mm)):
        for colum_idx in range(len(mm[row_idx])):
            print(mm[row_idx][colum_idx], end=" ")
            sum2 += mm[row_idx][colum_idx]
    print(f"\nSum = {sum2}")

matrix_elements(matrix)
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

# Print all elements in new list:
def flattering_matrix(mm):
    print("All elements by elements:")
    list_matrix = []
    for row in mm:
        for column in row:
            list_matrix.append(column)
    print(list_matrix, end=" ")

    print("\nAll elements by index:")
    list_matrix2 = []
    for row_idx in range(len(mm)):
        for column_idx in range(len(mm[row_idx])):
            list_matrix2.append(mm[row_idx][column_idx])
    print(list_matrix2, end=" ")

#flattering_matrix(matrix)