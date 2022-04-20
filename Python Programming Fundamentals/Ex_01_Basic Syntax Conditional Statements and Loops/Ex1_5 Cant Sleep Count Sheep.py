"""
Input	    Output
5	        1 sheep...2 sheep...3 sheep...4 sheep...5 sheep...
1	        1 sheep...
"""

number = int(input())

for i in range(1, number+1):
    print(f'{i} sheep...',end='')