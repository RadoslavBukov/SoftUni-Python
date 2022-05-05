"""
Input	                                                Output
High = 89#Low = 28#Medium = 77#Low = 23                 Cells:
1250                                                    - 89
                                                        - 28
                                                        - 77
                                                        - 23
                                                        Effort: 54.25
                                                        Total Fire: 217
"""
fire_level = str(input())
water = int(input())
list_fire_level = fire_level.split("#")
type_fire=''
value_of_cell = 0
effort = 0
total_fire = 0

print("Cells:")
for i in range(len(list_fire_level)):
    list_cell = list_fire_level[i].split(" = ")
    type_fire = list_cell[0]
    value_of_cell = int(list_cell[1])
    if water>=value_of_cell and ((type_fire == "High" and 81 <= value_of_cell <= 125) or (type_fire == "Medium" and 51 <= value_of_cell <= 80) or (type_fire == "Low" and 1 <= value_of_cell <= 50)):
        water -= value_of_cell
        effort += 0.25*value_of_cell
        total_fire += value_of_cell
        print(f"- {value_of_cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")