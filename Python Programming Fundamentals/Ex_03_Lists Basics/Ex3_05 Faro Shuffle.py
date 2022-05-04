"""
Input	                        Output
a b c d e f g h                 ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
5

one two three four              ['one', 'three', 'two', 'four']
3
"""
text = str(input())
count_of_shuffles = int(input())
text_list = text.split(" ")

for x in range (0, count_of_shuffles):
    first_half_list = []
    second_half_list = []
    shuffle_list = []
    elements = 0
    for i in range (0, len(text_list)):
        if i < len(text_list)/2:
            first_half_list.append(text_list[i])
        else:
            second_half_list.append(text_list[i])
    while elements < len(first_half_list):
        for j in range (0, len(first_half_list)):
            shuffle_list.append(first_half_list[j])
            shuffle_list.append(second_half_list[j])
            elements += 1
        text_list = shuffle_list
print(shuffle_list)