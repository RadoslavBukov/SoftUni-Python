"""
Input           Output                  Input       Output
7               Yes                     4           Yes
3               Sum = 12                6           Sum = 6
4                                       1
1                                       2
1                                       3
2
12
1

3               No                      3           No
1               Diff = 8                5           Diff = 8
1                                       5
10                                      1

3               No
1               Diff = 1
1
1
"""
import sys
n = int(input())

max_num = -sys.maxsize
sum_numbers = 0

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num

if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {sum_numbers - max_num}")
else:
    print("No")
    sum_others = sum_numbers - max_num
    print(f"Diff = {abs(max_num - sum_others)}")