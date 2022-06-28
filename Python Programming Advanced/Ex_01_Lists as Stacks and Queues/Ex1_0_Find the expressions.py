"""
Input
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

Output
(2 + 3)
(3 + 1)
(2 - (2 + 3) * 4 / (3 + 1))
"""
expression = input()
s = []

for j in range(len(expression)):
    if expression[j] == "(":
        s.append(j)
    elif expression[j] == ")":
        print(expression[s.pop():j+1])

 