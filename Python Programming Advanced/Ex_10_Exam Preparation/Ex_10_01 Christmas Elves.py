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
from collections import deque

elves_energy_input = list(map(int, input().split()))
material_box = list(map(int, input().split()))

elves_energy = deque()
total_energy = 0
toys = 0

for _ in elves_energy_input:
    elves_energy.append(_)

attemp_taking_box = 0
while material_box and elves_energy:
    elf_energy = elves_energy.popleft()
    if elf_energy < 5:
        continue
    material = material_box.pop()
    attemp_taking_box += 1

    if elf_energy >= material:
        if attemp_taking_box % 3 != 0 and attemp_taking_box % 5 != 0:
            toys += 1
            total_energy += material
            elf_energy = (elf_energy-material) + 1
            elves_energy.append(elf_energy)
        elif attemp_taking_box % 3 == 0 and attemp_taking_box % 5 != 0:
            if elf_energy >= material*2:
                toys += 2
                total_energy += material*2
                elf_energy = (elf_energy-(material*2)) + 1
                elves_energy.append(elf_energy)
            else:
                material_box.append(material)
                elf_energy *= 2
                elves_energy.append(elf_energy)
        elif attemp_taking_box % 3 != 0 and attemp_taking_box % 5 == 0:
            total_energy += material
            elf_energy -= material
            elves_energy.append(elf_energy)
    else:
        material_box.append(material)
        elves_energy.append(elf_energy * 2)

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")
if material_box:
    print(f"Boxes left: ",end="")
    print(', '.join([str(i) for i in material_box]))
elif elves_energy:
    print(f"Elves left: ", end="")
    print(', '.join([str(i) for i in elves_energy]))