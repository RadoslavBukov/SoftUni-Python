"""
Input	                                                    Output
SamsungA50, MotorolaG5, IphoneSE                            SamsungA50, MotorolaG5, Iphone10
Add - Iphone10
Remove - IphoneSE
End

HuaweiP20, XiaomiNote                                       HuaweiP20, XiaomiNote, Iphone5
Remove - Samsung
Bonus phone - XiaomiNote:Iphone5
End

SamsungA50, MotorolaG5, HuaweiP10                           MotorolaG5, HuaweiP10, SamsungA50
Last - SamsungA50
Add - MotorolaG5
End
"""
phone_list = input().split(", ")
command_input = input().split(" - ")
command = command_input[0]
phone = command_input[1]

while command != "End":
    if command == "Add":
        if phone not in phone_list:
            phone_list.append(phone)
    elif command == "Remove":
        if phone in phone_list:
            phone_list.remove(phone)
    elif command == "Bonus phone":
        old_new_phone = phone.split(":")
        old_phone = old_new_phone[0]
        new_phone = old_new_phone[1]
        if old_phone in phone_list:
            index = phone_list.index(old_phone)
            phone_list.insert(index+1,new_phone)
    elif command == "Last":
        if phone in phone_list:
            phone_list.remove(phone)
            phone_list.append(phone)
    command_input = input().split(" - ")
    command = command_input[0]
    if command != "End":
        phone = command_input[1]

print(f'{", ".join([str(i) for i in phone_list])}')