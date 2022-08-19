"""
Input	                    Output	                                            Comment
105 20 30 25                The wedding presents are made!                      First, we have 25 + 120 = 145, which is the needed product for a gemstone. Remove both.
120 60 11 400 10 1	        Magic left: 10, 1                                   30 + 60 = 90 (under 100 and even) => 30 * 2 + 60 * 3 = 240 which is the needed product for a porcelain sculpture. Remove both.
                            Gemstone: 1                                         20 + 11 = 31 (under 100 and odd) => 31 * 2 = 62 which is under 100 again so we remove both.
                            Porcelain Sculpture: 2	                            105 + 400 = 505 (more than 450) => 505 / 2 = 252.5 which is the needed product for a diamond porcelain sculpture. Remove both.
                                                                                We do not have any material left. The program ends. Print the desired text.

30 5 21 6 0 91              Aladdin does not have enough wedding presents.
15 9 5 15 8	                Materials left: 30
                            Gemstone: 1

200                         Aladdin does not have enough wedding presents.
5 15 32 20 10 5	            Magic left: 15, 32, 20, 10, 5
                            Porcelain Sculpture: 1
"""
from collections import deque

materials = list(map(int, input().split()))
magic_input = deque(map(int, input().split()))

presents_dict = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while materials and magic_input:
    material = materials.pop()
    magic = magic_input.popleft()
    initial_sum = material+magic
    sum = 0

    if initial_sum < 100:
        if initial_sum % 2 == 0: #Even
            sum = (2*material) + (3*magic)
        elif initial_sum % 2 != 0: #Odd
            sum = initial_sum*2
    elif initial_sum > 499:
        sum = initial_sum // 2
    else:
        sum = initial_sum

    if 100 <= sum <= 199:
        presents_dict["Gemstone"] += 1
    elif 200 <= sum <= 299:
        presents_dict["Porcelain Sculpture"] += 1
    elif 300 <= sum <= 399:
        presents_dict["Gold"] += 1
    elif 400 <= sum <= 499:
        presents_dict["Diamond Jewellery"] += 1

if (presents_dict["Gemstone"] > 0 and presents_dict["Porcelain Sculpture"] > 0) or (presents_dict["Gold"] > 0 and presents_dict["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: ",end="")
    print(', '.join([str(i) for i in materials]))
elif magic_input:
    print(f"Magic left: ", end="")
    print(', '.join([str(i) for i in magic_input]))

for present, quantity in sorted(presents_dict.items()):
    if quantity > 0:
        print(f"{present}: {quantity}")