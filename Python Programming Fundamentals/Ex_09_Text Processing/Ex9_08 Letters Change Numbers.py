"""
Input	                        Output	                        Comments
A12b s17G	                    330.00	                        12/1=12, 12+2=14, 17*19=323, 323–7=316, 14+316=330
P34562Z q2576f   H456z	        46015.12
a1A	                            0.00
"""
def letter_position(letter):
    lower_latter = letter.lower()
    position = ord(lower_latter) - 96

    return position

def letters(input_text):
    number_str = ""
    result = 0
    first_letter = input_text[0]
    second_letter = input_text[-1]

    for ch in input_text:
        if ch.isdigit():
            number_str += ch
            continue

    number = int(number_str)
    position_first_letter = letter_position(first_letter)
    position_second_letter = letter_position(second_letter)
    if first_letter.isupper():
        result = number / (position_first_letter)
    else:
        result = number * (position_first_letter)
    if second_letter.isupper():
        result -=  (position_second_letter)
    else:
        result += (position_second_letter)

    return result

total_result = 0
text = input().split()
for i in range(len(text)):
    total_result += letters(text[i])

print(f"{total_result:.2f}")

"""
#Working but not in judge!
while "  " in text:
    text = text.replace("  "," ")
list_text = text.split(" ")
"""

