"""
Input	                    Output	                        Comment
20 62 99 35 0 150           Total honey made: 148           First, compare 20 to 10. 20 is bigger than 10, so remove 10. Then compare 20 to 70. 20 is less than 70, so the bee could return to the hive.
120 60 10 1 70 10           Bees left: 99, 35, 0, 150       Honey made with given nectar is 20 + 70 = 90.
+ - + + / * - - /                                           Next, compare 62 to 1. 62 is bigger than 1, so remove 1. Compare 62 to 10. 62 is bigger than 10, so remove 10.
                                                            Compare 62 to 60. 62 is bigger than 60, so remove 60. Compare 62 to 120. 60 is less than 120, so the bee could return to the hive.
                                                            Honey made with given nectar is 62 - 120 = (-58). (-58) is negative, and its absolute value is 58, so the calculation result is 58.
                                                            Total honey made: 90 + 58 = 148. Print desired text.

30                          Total honey made: 4500
15 9 5 150 8                Nectar left: 15, 9, 5
* + + * -
"""
from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar_quantity = [int(x) for x in input().split()]
operators = deque([x for x in input().split()])

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
total_honey = 0
"""
while nectar_quantity and working_bees:
    bee = working_bees.popleft()
    nectar = nectar_quantity.pop()
    while nectar < bee and nectar_quantity:
        nectar = nectar_quantity.pop()
    operation = operators.popleft()
    if operation != "/" and nectar != 0:
        total_honey += abs(operations[operation](bee, nectar))
    if not nectar_quantity:
        working_bees.appendleft(bee)
"""
while nectar_quantity and working_bees:
    bee = working_bees.popleft()
    nectar = nectar_quantity.pop()

    if nectar < bee:
        working_bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operation = operators.popleft()
    total_honey += abs(operations[operation](bee, nectar))

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar_quantity:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_quantity])}")