"""
Input	        Output
5               The sum equals: 399
A
b
C
d
E
"""

number_of_lines = int(input())
symbol_sum = 0

for i in range (number_of_lines):
    letter = str(input())
    symbol_sum += ord(letter)

print(f"The sum equals: {symbol_sum}")