"""
Input	                        Output	                            Comments
52 74 23 44 96 110              Invalid placement!                  The first command is "Shoot", so we reduce the target on index 5, which is valid, with the given power – 10.
Shoot 5 10                      52|100                              Then we receive the same command, but we need to reduce the target on the 1st index, with power 80. The value of this target is 74, so it is considered shot, and we remove it.
Shoot 1 80                                                          Then we receive the "Strike" command on the 2nd index, and we need to check if the range with radius 1 is valid:
Strike 2 1                                                          52 23 44 96 100
Add 22 3                                                            And it is, so we remove the targets.
End	                                                                At last, we receive the "Add" command, but the index is invalid, so we print the appropriate message, and in the end, we have the following result:
                                                                    52|100

47 55 85 78 99 20               Strike missed!
Shoot 1 55                      22|47|50|40|85|78|99|20
Shoot 8 15
Strike 2 3
Add 0 22
Add 2 40
Add 2 50
End
"""
target_sequence = input().split(" ")
target_numbers = list(map(int,target_sequence))
command_input = input().split(" ")
command = command_input[0]
index = int(command_input[1])
value = int(command_input[2])

while command != "End":
    if command == "Shoot":
        if 0 <= index < len(target_numbers):
            if value < int(target_numbers[index]):
                target_numbers[index] -= value
            else:
                target_numbers.remove(target_numbers[index])
    elif command == "Add":
        if 0 <= index < len(target_numbers):
            target_numbers.insert(index,value)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        if index+value < len(target_numbers) and index-value >= 0:
            for i in range((index+value), (index-value-1), -1):
                target_numbers.remove(target_numbers[i])
        else:
            print("Strike missed!")

    command_input = input().split(" ")
    command = command_input[0]
    if command != "End":
        index = int(command_input[1])
        value = int(command_input[2])

print(f'{"|".join([str(i) for i in target_numbers])}')