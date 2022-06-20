"""
Input	                                                                Output
The _id and _age variables are both integers.	                        id,age
Calculate the _area of the _perfectRectangle object.	                area,perfectRectangle
__invalidVariable _evenMoreInvalidVariable_ _validVariable	            validVariable
"""
import re

text = input()
matches = re.findall(r"\b_[A-Za-z0-9]+\b", text)

words_list = []

for word in matches:
    words_list.append(word[1::])

print(",".join(words_list))