"""
Input	                Output

one
1
two
2                       1
Search                  {'one': 1}
one
Remove
two
End

one
two                     The variable number must be an integer
Search                  {}
Remove
End

one
1
Search                  1
one                     Number does not exist in dictionary
Remove                  {'one': 1}
two
End
"""
numbers_dictionary = {}

input_line = input()

while input_line != "Search":
    try:
        number_as_string = input_line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    input_line = input()

input_line = input()

while input_line != "Remove":
    try:
        searche = input_line
        print(numbers_dictionary[searche])
    except KeyError:
        print("Number does not exist in dictionary")
    input_line = input()

input_line = input()

while input_line != "End":
    try:
        searched = input_line
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    input_line = input()

print(numbers_dictionary)