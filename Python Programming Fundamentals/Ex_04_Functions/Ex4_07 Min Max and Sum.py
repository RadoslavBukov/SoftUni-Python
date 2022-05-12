"""
Input	                    Output
2 4 6	                    The minimum number is 2
                            The maximum number is 6
                            The sum number is: 12
12 52 11 53 2 8 45	        The minimum number is 2
                            The maximum number is 53
                            The sum number is: 183
"""
def values(list):
    int_list=[]
    for i in range(len(list)):
        int_list.append(int(list[i]))
    min_number = min(int_list)
    max_number = max(int_list)
    sum_number = sum(int_list)
    print(f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_number}")

input_list = input().split(" ")
values(input_list)