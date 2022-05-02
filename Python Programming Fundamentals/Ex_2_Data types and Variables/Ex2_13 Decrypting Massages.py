"""
Input	    Output              Input       Output
3           SoftUni             1           Decrypt
7                               7
P                               C
l                               d
c                               b
q                               q
R                               x
k                               o
f	                            s
"""

key = int(input())
n = int(input())
massage = ''

for i in range (n):
    letter = str(input())
    massage += chr(ord(letter) + key)
print(massage)
