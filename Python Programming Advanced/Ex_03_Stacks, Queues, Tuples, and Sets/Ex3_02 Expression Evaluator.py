"""
Input	                                    Output	                    Comment
6 3 - 2 1 * 5 /                             1                           6 - 3 = 3
                                                                        3 * 2 * 1 = 6
                                                                        6 / 5 = 1

2 2 - 1 *	                                0	                        2 - 2 = 0
                                                                        0 * 1 = 0
10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *	    164	                        10 * 23 = 230
                                                                        230 / 4 / 2 = 28
                                                                        28 + 30 + 10 = 68
                                                                        68 - 100 - 50 = -82
                                                                        -82 * 2 * -1 = 164
"""
from collections import deque

string_expression = input().split()
result = 0
nums = deque()

operations = {
    '+' : lambda a, b: a + b,
    '-' : lambda a, b: a - b,
    '*' : lambda a, b: a * b,
    '/' : lambda a, b: a // b,
}

for ch in string_expression:
    if ch in "+-*/":
        while len(nums) > 1:
            left = nums.popleft()
            right = nums.popleft()
            result = operations[ch](left,right)
            nums.appendleft(result)
    else:
        nums.append(int(ch))

print(nums.pop())