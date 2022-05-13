"""
Input	                Output		        Input	                Output
123, 323, 421, 121	    False               32, 2, 232, 1010        False
                        True                                        True
                        False                                       True
                        True                                        False
"""
def palindrome(list):
    for i in range(len(list)):
        if list[i] == list[i][::-1]:
            print("True")
        else:
            print("False")

input_list = input().split(", ")
palindrome(input_list)