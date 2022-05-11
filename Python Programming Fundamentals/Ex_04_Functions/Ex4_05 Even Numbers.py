"""
Input	            Output
1 2 3 4	            [2, 4]
1 2 3 -1 -2 -3	    [2, -2]
"""
def filter(list):
    even = []
    for i in range(len(list)):
        num = int(list[i])
        if num % 2 == 0:
            even.append(num)
    print(even)

input_list = input().split(" ")
filter(input_list)