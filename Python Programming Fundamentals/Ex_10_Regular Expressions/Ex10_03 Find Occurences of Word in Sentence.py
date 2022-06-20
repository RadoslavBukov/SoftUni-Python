"""
Input:	                                                                            Output:
The waterfall was so high, that the child couldn't see its peak.                    2
the
How do you plan on achieving that? How? How can you even think of that?             3
how
There was one. Therefore I bought it. I wouldn't buy it otherwise.                  1
there
"""
import re

text = input()
word = input()

matches = re.findall(rf"\b{word}\b", text, re.IGNORECASE)

print(f"{len(matches)}")