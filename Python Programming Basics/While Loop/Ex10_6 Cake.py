"""
Input           Output
10              No more cake left! You need 1 pieces more.
10
20
20
20
20
21

10              8 pieces are left.
2
2
4
6
STOP
"""
width = int(input())
length = int(input())
number_pieces = width*length

while number_pieces >= 0:
    pieces = str(input())
    if pieces == "STOP":
        print(f"{number_pieces} pieces are left.")
        break
    pieces_int = int(pieces)
    if number_pieces-pieces_int >=0:
        number_pieces -= pieces_int
    else:
        break
if pieces_int > number_pieces:
    print(f"No more cake left! You need {pieces_int - number_pieces} pieces more.")