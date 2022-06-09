"""
Input	             Output
text	             t -> 2
                     e -> 1
                     x -> 1

text text text       t -> 6
                     e -> 3
                     x -> 3
"""
text = input()
text = text.replace(" ","")
dictionary = dict()

for letter in text:
    if letter not in dictionary.keys():
        dictionary[letter] = 1
    else:
        dictionary[letter] += 1

for (key,value) in dictionary.items():
    print(f"{key} -> {value}")

"""
# 2nd Solution

from collections import Counter

text = input()
result = Counter(text)

for key,value in result.items():
    if key != " ":
        print(f'{key} -> {value}')
"""

