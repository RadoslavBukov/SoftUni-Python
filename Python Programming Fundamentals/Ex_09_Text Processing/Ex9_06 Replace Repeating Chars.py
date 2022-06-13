"""
Input	                        Output
aaaaabbbbbcdddeeeedssaa	        abcdedsa
qqqwerqwecccwd	                qwerqwecwd
"""
text = input()

for i in range(len(text)):
    if text[i] != text[i-1] or i==0:
        print(f"{text[i]}",end='')

# print("".join([text[i] for i in range(len(text)) if text[i] != text[i - 1] or i == 0]))