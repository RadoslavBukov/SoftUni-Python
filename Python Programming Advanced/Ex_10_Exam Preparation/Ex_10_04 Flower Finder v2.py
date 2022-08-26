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

vowels = deque(input().split())
consonants = deque(input().split())
words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
found_word = False

while vowels and consonants:
    v = vowels.popleft()
    c = consonants.pop()
    for word in words.keys():
        words[word] = words[word].replace(v, '')
        words[word] = words[word].replace(c, '')
        if words[word] == '':
            print(f"Word found: {word}")
            found_word = True
            break
    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")