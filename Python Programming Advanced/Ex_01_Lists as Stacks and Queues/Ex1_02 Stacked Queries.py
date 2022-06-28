"""
Input       Output                  Input       Output
9           26                      10          32
1 97        20                      2           66
2           91, 20, 26              1 47        8
1 20                                1 66        8, 16, 25, 32, 66, 47
2                                   1 32
1 26                                4
1 20                                3
3                                   1 25
1 91                                1 16
4                                   1 8
                                    4
"""
stack = []
lines = int(input())

for _ in range(lines):                          # "_", обхождаме дадена структура, без да ни трябва номера на обхождането
    queries = input()                           # Има въведена логика, която просто се изпълнява n на брой пъти
    if queries.startswith("1 "):
        number = (queries.split())[1]
        stack.append(int(number))
    elif queries == "2" and stack:
        stack.pop()
    elif queries == "3" and stack:
        print(max(stack))
    elif queries == "4" and stack:
        print(min(stack))

while stack:
    if len(stack) > 1:
        print(stack.pop(), end=', ')
    else:
        print(stack.pop())