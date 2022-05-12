"""
Input	                Output
6 2 4	                [2, 4, 6]
12 52 11 53 2 8 45	    [2, 8, 11, 12, 45, 52, 53]
"""
def sort(list):
    sorted_list=[]
    for i in range(len(list)):
        sorted_list.append(int(list[i]))
    sorted_list.sort()
    print(sorted_list)

input_list = input().split(" ")
sort(input_list)