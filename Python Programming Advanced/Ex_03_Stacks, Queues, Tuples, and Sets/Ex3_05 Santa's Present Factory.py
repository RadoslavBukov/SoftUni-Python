"""
Input	                    Output	                                            Comment
10 -5 20 15 -30 10          The presents are crafted! Merry Christmas!          First, we have 40*10=400, which is the needed magic for a bicycle. Remove both.
40 60 10 4 10 0	            Materials left: 20, -5, 10                          60*(-30) = -1800 (negative). 60+(-30) = 30. Remove 60 and -30. Add 30 to materials.
                            Bicycle: 1                                          30*10=300 (bear). Remove both.
                            Teddy bear: 2                                       4*15=60, so remove 4, and the material is increased by 15 (15+15=30).
                                                                                10*30=300 (bear).
                                                                                Print desired text.

30 5 15 60 0 30             No presents this Christmas!
-15 10 5 -15 25	            Materials left: 20, 30
                            Doll: 1
                            Teddy bear: 1

30 10                       No presents this Christmas!
15 10 5 0 10	            Magic left: 5, 0, 10
                            Doll: 1
                            Teddy bear: 1
"""
from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

crafting_table = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_toys = {}

while materials and magic_values:
    material = materials.pop()
    value = magic_values.popleft()

    if material == 0 and value == 0:
        continue

    if material == 0:
        magic_values.appendleft(value)

    if value == 0:
        materials.append(material)
        continue

    result = material * value
    if result in crafting_table:
        toy_name = crafting_table[result]
        if toy_name in crafted_toys:
            crafted_toys[toy_name] += 1
        else:
            crafted_toys[toy_name] = 1
        continue

    if result < 0:
        materials.append(material+value)
    else:
        materials.append(material+15)

if ("Doll" in crafted_toys and "Wooden train" in crafted_toys) or ("Teddy bear" in crafted_toys and "Bicycle" in crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for toy, count in sorted(crafted_toys.items()):
    print(f"{toy}: {count}")