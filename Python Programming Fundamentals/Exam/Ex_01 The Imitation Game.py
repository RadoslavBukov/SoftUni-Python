"""
Input	            Output
zzHe                The decrypted message is: Hello
ChangeAll|z|l
Insert|2|o
Move|3
Decode

owyouh              The decrypted message is: howareyou?
Move|2
Move|3
Insert|3|are
Insert|9|?
Decode
"""
encrypred_text = input()
instructions = input().split("|")
decrypted_text = ""

while instructions[0] != "Decode":
    if instructions[0] == "Move":
        number_letters = int(instructions[1])
        encrypred_text = encrypred_text[number_letters:len(encrypred_text)+1]+encrypred_text[0:number_letters]
    elif instructions[0] == "Insert":
        index = int(instructions[1])
        value = instructions[2]
        encrypred_text = encrypred_text[0:index]+value+encrypred_text[index:len(encrypred_text)+1]
    elif instructions[0] == "ChangeAll":
        substring = instructions[1]
        replacement = instructions[2]
        encrypred_text = encrypred_text.replace(substring,replacement)

    instructions = input().split("|")

print(f"The decrypted message is: {encrypred_text}")