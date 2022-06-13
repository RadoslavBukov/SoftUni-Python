"""
Input	                                Output	                        Comments
abv>1>1>2>2asdasd	                    abv>>>>dasd	                    1st explosion is at index 3, with a strength of 1. We delete only the digit after the explosion character.
                                                                            The string will look like this: abv>>1>2>2asdasd
                                                                        2nd explosion is with strength one, and the string transforms to this: abv>>>2>2asdasd
                                                                        3rd explosion is now with a strength of 2. We delete the digit, and we find another explosion.
                                                                            At this point, the string looks like this: abv>>>>2asdasd.
                                                                        4th explosion is with strength 2. We have 1 strength left from the previous explosion, and we add the
                                                                            strength of the current explosion to what is left, which adds up to a total strength of 3.
                                                                            We delete the next three characters, and we receive the string abv>>>>dasd
                                                                        We do not have any more explosions, and we print the result: abv>>>>dasd

pesho>2sis>1a>2akarate>4hexmaster	    pesho>is>a>karate>master
"""
import string
text = input()
result_text = ""
explosion = 0
jump = 0

for i in range(len(text)):
    i += jump
    if i >= len(text):
        break
    if text[i] in string.ascii_letters:
        result_text += text[i]
    if text[i] == ">":
        result_text += text[i]
    if text[i].isdigit() and text[i-1] == ">":
        if int(text[i]) + explosion > 1:
            explosion = explosion + int(text[i]) - 1
            for j in range(i+1, i+explosion+1):
                if j >= len(text):
                    break
                if text[j] == ">":
                    break
                else:
                    explosion = explosion - 1
                    jump += 1
print(result_text)


"""
text = input()
new_text = list()
strength = 0
 
for ch in text:
    if ch.isdigit():
        strength += int(ch)
        strength -= 1
        continue
    else:
        if strength < 1:
            new_text.append(ch)
        else:
            if ch == ">":
                new_text.append(ch)
            else:
                strength -= 1
                continue
print("".join(new_text))
"""