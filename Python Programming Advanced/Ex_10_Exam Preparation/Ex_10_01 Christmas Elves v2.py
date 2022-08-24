"""
Input	                Output	                        Comment
10 16 13 25             Toys: 3                         1) The elf with energy 10 takes the box with 8 materials. He creates 1 gift and uses 8 units of energy. He eats a cookie and goes to the end of the line, which now looks like this: 16 13 25 3.
12 11 8	                Energy: 31                      2) The elf with energy 16 takes the box with 11 materials. He creates 1 gift and uses 11 units of energy. Then, he eats a cookie and goes to the end of the line, which now looks like this: 13 25 3 6.
                        Elves left: 3, 6, 26, 14	    3) The elf with energy 13 takes the box with 12 materials. It is the third time an elf takes a box. The elf does not have the needed energy: 12 * 2, so he drinks a hot chocolate and goes to the end of the line: 25 3 6 26.
                                                        4) The elf with energy 25 takes the box with 12 materials. It is the fourth time an elf takes a box. He creates 1 gift and uses 12 units of energy. He eats a cookie and goes to the end of the line, which now looks like this: 3 6 26 14.
                                                        No boxes are left, so the program ends. Print the desired text.
10 14 22 4 5            Toys: 7
11 16 17 11 1 8         Energy: 75
                        Elves left: 10, 14

5 6 7                   Toys: 3
2 1 5 7 5 3	            Energy: 20
                        Boxes left: 2, 1
"""
'''
import sys
from collections import deque
from io import StringIO

'''
"""
elves: 10 16 13 25
boxes: 12 11 8

# Turn 1 - elf 10, box 8
total_energy = 8
toys_count = 1

elves: 16 13 25   (2+1)=3
boxes: 12 11

# Turn 2 - elf 16, box 11
total_energy = 8 + 11 = 19
toys_count = 1 + 1 = 2

elves: 13 25  3  (5+1)=6
boxes: 12

# Turn 3 - elf 13, box 12
total_energy = 19
toys_count = 2

elves: 25  3 6 (13*2)=26
boxes: 12

# Turn 4 - elf 25, box - 12
total_energy = 19 + 12 = 31
toys_count = 3

elves: 3 6 26 (13+1)=14
boxes: (empty)
'''

test_input_1 = '''10 16 13 25
12 11 8
'''

test_input_2 = '''10 14 22 4 5
11 16 17 11 1 8
'''

test_input_3 = '''5 6 7
2 1 5 7 5 3
'''

# sys.stdin = StringIO(test_input_1)
# sys.stdin = StringIO(test_input_2)
# sys.stdin = StringIO(test_input_3)
"""

from collections import deque
elf_energies = deque([int(x) for x in input().split(' ')])
boxes = [int(x) for x in input().split(' ')]
turns_count = 0
total_energy_spent = 0
toys_count = 0

while boxes and elf_energies:
    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()

    if not elf_energies:
        break

    box = boxes.pop()
    elf_energy = elf_energies.popleft()

    turns_count += 1

    toys_to_be_created_count = 1
    energy_to_be_spent = box
    energy_increase_factory = 1

    if turns_count % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spent *= 2
    if turns_count % 5 == 0:
        toys_to_be_created_count = 0
        energy_increase_factory = 0

    if energy_to_be_spent <= elf_energy:
        toys_count += toys_to_be_created_count
        total_energy_spent += energy_to_be_spent
        elf_energies.append(elf_energy - energy_to_be_spent + energy_increase_factory)
    else:
        boxes.append(box)
        elf_energies.append(elf_energy * 2)

print(f'Toys: {toys_count}')
print(f'Energy: {total_energy_spent}')
if elf_energies:
    elves_string = ', '.join(str(x) for x in elf_energies)
    print(f'Elves left: {elves_string}')
if boxes:
    boxes_string = ', '.join(str(x) for x in boxes)
    print(f'Boxes left: {boxes_string}')