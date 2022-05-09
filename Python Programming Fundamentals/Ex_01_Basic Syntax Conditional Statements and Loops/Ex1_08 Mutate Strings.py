"""
Input	                Output
bubble gum              tubble gum
turtle hum	            turble gum
                        turtle gum
                        turtle hum

Kitty                   Ditty
Doggy	                Dotty
                        Dogty
                        Doggy
"""
string1 = str(input())
string2 = str(input())
mix_string = ''

for char in range(0, len(string1)):
    if string1[char] != string2[char]:
        mix_string = string2[:char+1] + string1[char+1:]
        print(mix_string)