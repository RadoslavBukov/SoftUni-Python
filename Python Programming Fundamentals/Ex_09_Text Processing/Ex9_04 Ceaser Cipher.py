"""
Input	                    Output

Programming is cool!	    Surjudpplqj#lv#frro$
One year has 365 days.	    Rqh#|hdu#kdv#698#gd|v1
"""
input_text = input()
output_text = ""

for letter in input_text:
    output_text += chr(ord(letter) + 3)

print(output_text)