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
first_sequence = set(input().split())
second_sequence = set(input().split())
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            for i in range(2, len(command)):
                first_sequence.add(command[i])
        else:
            for i in range(2, len(command)):
                second_sequence.add(command[i])
    elif command[0] == "Remove":
        if command[1] == "First":
            for i in range(2, len(command)):
                if command[i] in first_sequence:
                    first_sequence.remove(command[i])
        else:
            for i in range(2, len(command)):
                if command[i] in second_sequence:
                    second_sequence.remove(command[i])
    elif command[0] == "Check":
        if first_sequence < second_sequence or second_sequence < first_sequence:
            print("True")
        else:
            print("False")

print(", ".join(sorted(first_sequence)))
print(", ".join(sorted(second_sequence)))