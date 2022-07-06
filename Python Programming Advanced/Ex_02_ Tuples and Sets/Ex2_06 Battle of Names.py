"""
Input	        Output	                    Comment
4               304, 128, 206, 511          First name: Pesho. The sum of the ASCII values is: 80 + 101 + 115 + 104 + 111 = 511. Integer divide the sum to the current row (1): 511 / 1 = 511.
Pesho                                       Second name: Stefan. The sum of the ASCII values is: 83 + 116 + 101 + 102 + 97 + 110 = 609. Integer divide the sum to the current row (2): 609 / 2 = 304.
Stefan                                      Third name: Stamat. The sum of the ASCII values is: 83 + 116 + 97 + 109 + 97 + 116 = 618. Integer divide the sum to the current row (3): 618 / 3 = 206.
Stamat                                      Fourth name: Gosho. The sum of the ASCII values is: 71 + 111 + 115 + 104 + 111 = 512. Integer divide the sum to the current row (4): 512 / 4 = 128.
Gosho		                                The odd set: 511
                                            The even set: 304, 206, 128
                                            The sum of the even numbers is larger, so we print the symmetric-different values.

6
Preslav         733, 101
Gosho
Ivan
Stamat
Pesho
Stefan
"""
n = int(input())
even_set = set()
odd_set = set()

for current_row in range(1, n+1):
    name = input()
    ascii_value = 0
    for char in name:
        ascii_value += ord(char)
    divided_number = ascii_value // current_row
# Variant 2, replacing the for cycle
#   divided_number = sum([ord(x) for x in name] // current_row)
    if divided_number % 2 == 0:
        even_set.add(divided_number)
    else:
        odd_set.add(divided_number)

if sum(even_set) == sum(odd_set):
    result = even_set|odd_set
    print(', '.join([str(i) for i in result]))
elif sum(odd_set) > sum(even_set):
    result = odd_set - even_set
    print(', '.join([str(i) for i in result]))
else:
    result = even_set ^ odd_set
    print(', '.join([str(i) for i in result]))
#   print(*result, sep=", ")