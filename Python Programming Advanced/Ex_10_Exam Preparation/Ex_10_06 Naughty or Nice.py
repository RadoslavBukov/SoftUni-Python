"""
Test Code	                                Output

print(naughty_or_nice_list(                 Nice: Amy
    [                                       Naughty: Tom, Katy
        (3, "Amy"),                         Not found: George
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
"""
def naughty_or_nice_list(santas_list,*args, **kwargs):
    nice, naughty, not_found = [], [], []

    for string in args:
        num, status = string.split("-")
        num = int(num)
        name = ''

        only_number = False
        for kid_number, kid_name in santas_list:
            if kid_number == num and only_number:
                only_number = False
                break
            elif kid_number ==num:
                name = kid_name
                only_number = True

        if only_number:
            santas_list.remove((num, name))

            if status == "Nice":
                nice.append(name)
            elif status == "Naughty":
                naughty.append(name)

    for key, value in kwargs.items():
        number = ''

        unique_name = False
        for kid_number, kid_name in santas_list:
            if key == kid_name and unique_name:
                unique_name = False
                break
            elif key == kid_name:
                number = kid_number
                unique_name = True

        if unique_name:
            santas_list.remove((int(number),key))

            if value == "Nice":
                nice.append(key)
            elif value == "Naughty":
                naughty.append(key)

    if santas_list:
        for number, name in santas_list:
            not_found.append(name)


    result = ""
    if nice:
        result += f"Nice: {', '.join(str(x) for x in nice)}\n"
    if naughty:
        result += f"Naughty: {', '.join(str(x) for x in naughty)}\n"
    if not_found:
        result += f"Not found: {', '.join(str(x) for x in not_found)}"

    return result

# Input 1
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

# Input 2
# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))

# Input 3
# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
