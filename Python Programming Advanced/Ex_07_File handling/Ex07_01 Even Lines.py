"""
Input                           Output
Ex07_01 Even Lines.txt          fault@ his wasn't it but him@ judge to quick was @I
                                safer@ is It here@ hide @Quick@
"""
symbols = ["-", ",", ".", "!", "?"]
file_path = "./Ex07_01 Even Lines.txt"

with open(file_path, 'r') as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            result = " ".join(line.strip().split()[::-1])
            for symbol in symbols:
                result = result.replace(symbol, '@')
            print(result)