"""
Input	                Output
1 2 -3 -3 5	            [-1, -2, 3, 3, -5]
-4 0 2 57 -101	        [4, 0, -2, -57, 101]
"""

string = str(input())
oposite_list = []
list = string.split(" ")

for element in list:
    oposite_list.append(-(int(element)))
print(oposite_list)