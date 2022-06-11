"""
Input	                                                                                            Output
There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)	        :P
                                                                                                    :O
                                                                                                    :)
"""
text = input()

emoticon = [text[i] + text[i+1] for i in range(len(text)) if text[i] == ":" and text[i+1] != " "]
print('\n'.join(emoticon))

"""
text = input().split(":")
symbols= ["", " ", "\t", "\n"]

for i in range(1, len(text)):
    for letter in text[i]:
        if letter not in symbols:
            print(f":{letter}")
            break
        else:
            break
"""