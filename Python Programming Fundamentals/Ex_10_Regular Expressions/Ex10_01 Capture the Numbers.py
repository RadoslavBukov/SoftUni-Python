"""
Input	                            Output

The300                              300 3 22 45
What is that?
I think it's the 3rd movie
Let's watch it at 22:45

123a456                             123 456 789 987 654 321 0
789b987
654c321
0

Let's go11!!!11!                    11 11 1
Okey!1!
"""
import re

while True:
    text = input()

    if not text:
        break

    matches = re.findall(r"\d+", text)

    if len(matches) > 0:
        print(" ".join(matches), end=" ")