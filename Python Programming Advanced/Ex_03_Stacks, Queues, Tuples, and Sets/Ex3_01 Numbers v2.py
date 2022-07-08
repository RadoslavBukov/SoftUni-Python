"""
Input	                    Output
1 2 3 4 5                   True
1 2 3                       1, 2, 3, 4, 5, 6
3                           1, 2, 3
Add First 5 6
Remove Second 8 9 11
Check Subset

5 4 2 9 9 5 4               False
1 1 1 5 6 5                 2, 3, 4, 5, 6, 9
4                           6
Add First 5 6 9 3
Add Second 1 2 3 3 3
Check Subset
Remove Second 1 2 3 4 5
"""
first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    command_input = input().split()
    command = command_input[0]
    target_set = command_input[1]
    if command == "Add":
        if target_set == "First":
            first_sequence = first_sequence.union([int(x) for x in command_input[2:]])
        else:
            second_sequence = second_sequence.union([int(x) for x in command_input[2:]])
    elif command == "Remove":
        if target_set == "First":
            first_sequence = first_sequence.difference([int(x) for x in command_input[2:]])
        else:
           second_sequence = second_sequence.difference([int(x) for x in command_input[2:]])
    elif command == "Check":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=", ")