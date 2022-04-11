"""
Input           Output              Input       Output
7               1	                12          1
                2 3                             2 3
                4 5 6                           4 5 6
                7                               7 8 9 10

10	            1                   15          1
                2 3                             2 3
                4 5 6                           4 5 6
                7 8 9 10                        7 8 9 10
                                                11 12 13 14 15
"""
n = int(input())
current = 1
current_bigger_than_n = False

for row in range(1, n+1):
    for col in range(1, row+1):
        if current > n:
            current_bigger_than_n = True
            break
        print(f"{current}"+'', end=' ')
        current += 1
    if current_bigger_than_n:
        break
    print()
