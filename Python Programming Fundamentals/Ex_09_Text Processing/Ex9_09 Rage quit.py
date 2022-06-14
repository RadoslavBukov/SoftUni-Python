"""
Input	            Output	                            Comments
a3	                Unique symbols used: 1              We have just one string-number pair. The symbol is 'a', convert it to uppercase and repeat 3 times: AAA.
                    AAA	                                Only one symbol is used ('A').

aSd2&5s@1	        Unique symbols used: 5              "aSd" is converted to "ASD" and repeated twice; "&" is repeated 5 times; "s@" is converted to "S@" and repeated once.
                    ASDASD&&&&&S@	                    5 symbols are used: 'A', 'S', 'D', '&' and '@'.
"""
text = input()
symbols = ""
number = ""
unique_symbols = []
result = ""
shibanata_dylzhina = len(text)
last_element = len(text) -1

for i in range(len(text)):
    a = text[i]
    if not text[i].isdigit():
        symbols += text[i]
        if text[i].upper() not in unique_symbols:
            unique_symbols.append(text[i].upper())
    elif text[i].isdigit():
        if i <= last_element:
            if text[i+1].isdigit():
                number += text[i]
            else:
                number += text[i]
                result += symbols.upper() * int(number)
                number = 0
                symbols = ""
        else:
                number += text[i]
                result += symbols.upper() * int(number)
                number = 0
                symbols = ""

print(f"Unique symbols used: {len(unique_symbols)}")
print(result)

"""
#Working
import re

input_string = input().upper()

splitted_input = re.split(r"(\d+)", input_string)
result_list = []

for i in range(0, len(splitted_input) - 1, 2):
    string_to_repeat = splitted_input[i]
    repeat_times = int(splitted_input[i + 1])
    result_list.append(string_to_repeat * repeat_times)

result_to_print = ''.join(result_list)
unique_characters = len(set(result_to_print))

print(f"Unique symbols used: {unique_characters}")
print(result_to_print)
"""