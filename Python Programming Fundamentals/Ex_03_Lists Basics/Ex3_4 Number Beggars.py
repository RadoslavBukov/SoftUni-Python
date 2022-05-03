"""
Input	                        Output
1, 2, 3, 4, 5                   [9, 6]
2

3, 4, 5, 1, 29, 4               [3, 4, 5, 1, 29, 4]
6

100, 94, 24, 99                 [100, 94, 24, 99, 0]
5
"""
line1 = str(input())
count_of_beggar = int(input())
line1_list = line1.split(", ")
beggars_list = []
offers = 0

for i in range (count_of_beggar):
    beggars_list.append(0)

while offers < len(line1_list):
    for j in range(len(beggars_list)):
        if offers >= len(line1_list):
            break
        beggars_list[j] += int(line1_list[offers])
        offers += 1
print(beggars_list)