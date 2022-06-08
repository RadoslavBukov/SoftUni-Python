"""
Input	                    Output
Peter-Java-84               Results:
George-C#-84                Peter | 84
George-C#-70                George | 84
Katy-C#-94                  Katy | 94
exam finished	            Submissions:
                            Java - 1
                            C# - 3

Peter-Java-91               Results:
George-C#-84                Peter | 91
Katy-Java-90                George | 84
Katy-C#-50                  Submissions:
Katy-banned                 Java - 2
exam finished	            C# - 2
"""
text = input()
users_dict = {}
language_dict = {}

while text != "exam finished":
    if not "banned" in text:
        text = text.split("-")
        username = text[0]
        language = text[1]
        points = int(text[2])

        if username not in users_dict.keys():
            users_dict[username] = points
        else:
            if points > users_dict[username]:
                users_dict[username] = points

        if language not in language_dict.keys():
            language_dict[language] = 1
        else:
             language_dict[language] += 1

    else:
        text = text.split("-")
        username = text[0]
        users_dict.pop(username)
    text = input()

print("Results:")
for (key, value) in users_dict.items():
    print(f"{key} | {value}")
print("Submissions:")
for (key, value) in language_dict.items():
    print(f"{key} - {value}")