"""
Input                                   Output
5 4 8 6 3 8 7 7 9                       5
16

1 7 8 2 5 4 7 8 9 6 3 2 5 4 6           5
20
"""
# Variant 2
# clothes_in_box = list(map(int, input().split()))
clothes_in_box = [int(x) for x in input().split()]
rack_capacity_initial = int(input())
rack_capacity = rack_capacity_initial
number_racks_needed = 1

while clothes_in_box:
    if clothes_in_box[-1] <= rack_capacity:
        rack_capacity -= clothes_in_box.pop()
    else:
        number_racks_needed += 1
        rack_capacity = rack_capacity_initial

print(number_racks_needed)