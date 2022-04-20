"""
Input	        Output
Hello           World	HHeelllloo  WWoorrlldd
1234!	        11223344!!
"""

word = str(input())
double_string = ''

for char in range(len(word)):
    double_string += (word[char]*2)
print(double_string)