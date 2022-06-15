"""
Input	            Output
George Peter	    52114
123 522	            7647
a aaaa	            9700
"""
def multiply(first_word, second_word):
    result = 0
    for i in range(0, len(first_word)):
        if i < len(second_word):
            result += ord(first_word[i]) * ord(second_word[i])
        else:
            result += ord(first_word[i])
    print(result)

text = input().split(" ")

if len(text[0]) > len(text[1]):
    multiply(text[0], text[1])
else:
    multiply(text[1], text[0])