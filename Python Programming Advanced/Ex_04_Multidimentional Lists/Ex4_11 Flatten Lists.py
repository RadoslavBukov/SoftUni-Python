"""
Input	                        Output
1 2 3 |4 5 6 |  7  88	        7 88 4 5 6 1 2 3
7 | 4  5|1 0| 2 5 |3	        3 2 5 1 0 4 5 7
1| 4 5 6 7  |  8 9	            8 9 4 5 6 7 1
"""
lists = input().split("|")
list_elements = []

for list in lists:
    elements = list.split()
    list_elements.append(elements)

for index in range(len(list_elements)-1,-1,-1):
    for element in list_elements[index]:
       print(element, end=" ")

"""
Variant2

lists = input().split("|")
result = []

for idx in range(len(sublists))-1, -1, -1):
    current_elements = sublists[idx].strip().split()
    result.extend(current_elements)

print(' '.join(result))
"""