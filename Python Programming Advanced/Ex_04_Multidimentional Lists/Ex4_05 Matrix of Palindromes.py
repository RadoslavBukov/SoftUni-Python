"""
Input	    Output
4 6	        aaa aba aca ada aea afa
            bbb bcb bdb beb bfb bgb
            ccc cdc cec cfc cgc chc
            ddd ded dfd dgd dhd did

3 2	        aaa aba
            bbb bcb
            ccc cdc
"""
rows, columns = [int(x) for x in input().split()]
char = ord("a")

for row in range(rows):
    ll = []
    for column in range(columns):
        ll.append(chr(char+row)+chr(char+row+column)+chr(char+row))
    print(" ".join(ll))