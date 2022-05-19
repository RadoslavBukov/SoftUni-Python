"""
Input	                    Output
72olle 103doo 100ya	        Hello good day
82yade 115te 103o	        Ready set go
"""
input_massage = input().split(" ")
letter_list = []
digit_list = []
decrypt_word = []

def decrypt(word):
    letter_list.clear()
    digit_list.clear()
    decrypt_word.clear()
    for letter in word:
        if letter.isdigit():
            digit_list.append(letter)
        else:
            letter_list.append(letter)
    letter_list[0], letter_list[-1] = letter_list[-1], letter_list[0]
    int_digit = int("".join(digit_list))
    decrypt_word.append(chr(int_digit))
    decrypt_word.extend(letter_list)
    print(f'{"".join([str(i) for i in decrypt_word])}',end=" ")

for i in input_massage:
    decrypt(i)