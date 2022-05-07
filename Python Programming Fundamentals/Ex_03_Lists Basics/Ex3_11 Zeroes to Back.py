"""
Input	                    Output
1, 0, 1, 2, 0, 1, 3	        [1, 1, 2, 1, 3, 0, 0]
0, 5, 0, 4, 0, 0, 5	        [5, 4, 5, 0, 0, 0, 0]
"""

input_list = input().split(", ")
new_list = []
zeros = 0

for i in range(len(input_list)):
    if int(input_list[i]) > 0:
        new_list.append(int(input_list[i]))
    else:
        zeros += 1
for j in range(zeros):
    new_list.append(0)

print(new_list)