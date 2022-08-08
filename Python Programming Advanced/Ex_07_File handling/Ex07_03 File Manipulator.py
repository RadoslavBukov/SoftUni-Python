"""
Input	                                    Comment
Create-file.txt                             The first command creates the empty file
Add-file.txt-First Line                     After the first and second Add command, the content is:
Add-file.txt-Second Line                    First Line
Replace-random.txt-Some-some                Second Line
Replace-file.txt-First-1st                  On the first Replace command, an error must occur
Replace-file.txt-Second-2nd                 After the next two Replace commands, the content is:
Delete-random.txt                           1st Line
Delete-file.txt                             2nd Line
End	                                        After the first Delete command, an error occurs
                                            Finally, the 'file.txt' file is deleted
"""
import os
from os.path import exists

while True:
    command_line = input()

    if command_line == "End":
        break
    command_parts = command_line.split("-")
    command, file_name = command_parts[0], command_parts[1]
    if command == "Create":
        with open(f"./{file_name}", "w") as file:
            pass
    elif command == "Add":
        content = command_parts[2]
        with open(f"./{file_name}", "a") as file:
            file.write(f"{content}\n")
    elif command == "Replace":
        if not exists(f"./{file_name}"):
            print("An error occurred.")
            continue
        old_string, new_string = command_parts[2], command_parts[3]
        with open(f"./{file_name}", "r+") as file:
            file_content = file.read().replace(old_string, new_string)
            # Moving the pointer to the beginning of the file:
            file.seek(0)
            # Clearing the file from the pointer to the end of the file:
            file.truncate()
            file.write(file_content)

    elif command == "Delete":
        if not exists(f"./{file_name}"):
            print("An error occurred.")
            continue
        os.remove(f"{file_name}")