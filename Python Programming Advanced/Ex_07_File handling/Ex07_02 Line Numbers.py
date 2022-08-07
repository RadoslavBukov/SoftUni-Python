"""
Input                           Output
Ex07_02 Line Numbers.txt        Ex07_02 Line Numbers_output.txt
                                Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
                                Line 2: -Is this some kind of joke?! Is it? (24)(4)
                                Line 3: -Quick, hide here. It is safer. (22)(4)
"""
from string import punctuation

def SymbolCount(text_line):
    letter_count = 0
    punctation_count = 0
    for symbol in text_line:
        if symbol.isalpha():
            letter_count += 1
        elif symbol in punctuation:
            punctation_count += 1
    return letter_count, punctation_count

with open('./Ex07_02 Line Numbers.txt') as file, open("./Ex07_02 Line Numbers_output.txt", "w") as output_file:
    for idx, line in enumerate(file):
        letter_count, punctation_count = SymbolCount(line)
        output_file.write(f"Line {idx+1}: {line.strip()} ({letter_count})({punctation_count})\n")
