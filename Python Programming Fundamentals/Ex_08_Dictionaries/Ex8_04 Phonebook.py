"""
Input	                            Output
Adam-0888080808                     Contact Mery does not exist.
2                                   Adam -> 0888080808
Mery
Adam

Adam-+359888001122                  Silvester -> 02/987665544
Ralf-666                            Contact silvester does not exist.
George-5559393                      Contact Rolf does not exist.
Silvester-02/987665544              Ralf -> 666
4
Silvester
silvester
Rolf
Ralf
"""
contact = input().split("-")
phonebook = dict()

while len(contact) > 1:
    name = str(contact[0])
    number = str(contact[1])
    phonebook[name] = number
    contact = input().split("-")

search = int(contact[0])

for i in range(0,search):
    searching_name = input()
    if searching_name in phonebook.keys():
        print(f"{searching_name} -> {phonebook[searching_name]}")
    else:
        print(f"Contact {searching_name} does not exist.")

"""
# 2nd Solution

def phone_book_information(number_of_lines, phone_book):
    for i in range(number_of_lines):
        name = input()
        if name not in phone_book:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phone_book[name]}")
    return True

def phone_book_info():
    phone_book = {}
    conditions = False
    while True:
        contact_information = input().split('-')
        if contact_information[0].isdigit():
            conditions = phone_book_information(int(contact_information[0]), phone_book)
        else:
            phone_book[contact_information[0]] = contact_information[1]
        if conditions:
            break

phone_book_info()
"""