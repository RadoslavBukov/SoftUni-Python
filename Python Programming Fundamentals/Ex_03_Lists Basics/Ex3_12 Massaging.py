"""
Input	                            Output
9992 562 8933                       Hey
This is some message for you

2 122 1123 1321 9 17211             Judge!
87j973u59dg37e725!
"""
input_list = input().split(" ")
input_string = str(input())
list_string = []
number_count = 0
new_list = []

for char in input_string:
    list_string.append(char)

while number_count < len(input_list):
    for i in range(len(input_list)):
        sum_of_digits = 0
        for digit in input_list[i]:
            sum_of_digits += int(digit)
        if sum_of_digits <= len(list_string):
            new_list.append(list_string[sum_of_digits])
            list_string.pop(sum_of_digits)
        else:
            sum_of_digits -= len(list_string)
            new_list.append(list_string[sum_of_digits])
            list_string.pop(sum_of_digits)
        number_count += 1

print(f'{"".join([str(i) for i in new_list])}')