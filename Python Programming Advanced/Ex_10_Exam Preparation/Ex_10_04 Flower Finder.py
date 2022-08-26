"""
Input	                        Output                              Comment
o e a o e a i                   Word found: rose                    Start by taking the first volew "o" and the last consonant "r". They are found in words "rose", "lotus", and "daffodil".
p r s x r	                    Vowels left: o e a i                Then, take "e" and "x". They are found in the word "rose".
                                Consonants left: p r                Then, take "a" and "s". They are found in words "rose", "lotus", and "daffodil".
                                                                    The word "rose" is found, so we print it. Then we print the remaining letters in each sequence.

a a a                           Cannot find any word!
x r l t p p	                    Consonants left: x r l

u a o i u y o e                 Word found: tulip
p m t l	                        Vowels left: u y o e
"""
from collections import deque

def check_word(char, dict, flower):
    if char in dict:
        dict[char] = True
    if all(dict.values()):
        print(f"Word found: {flower}")
        return True

flowers = ["rose", "tulip", "lotes", "daffodil"]
rose = {letter: False for letter in "rose"}
tulip = {letter: False for letter in "tulip"}
lotus = {letter: False for letter in "lotus"}
daffodil = {letter: False for letter in "daffodil"}

vowel = deque(input().split())
consonants = input().split()
flower_found = False

while vowel and consonants:
    vowel_letter = vowel.popleft()
    consonants_letter = consonants.pop()

    for flower in flowers:
        if flower == "rose":
            dict_output = rose
        elif flower == "tulip":
            dict_output = tulip
        elif flower == "lotus":
            dict_output = lotus
        elif flower == "daffodil":
            dict_output = daffodil

        if check_word(vowel_letter, dict_output, flower):
            flower_found = True
            break
        if check_word(consonants_letter, dict_output, flower):
            flower_found = True
            break
    if flower_found:
        break

if not flower_found:
    print(f"Cannot find any word!")

if vowel:
    print(f"Vowels left: {' '.join(vowel)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")