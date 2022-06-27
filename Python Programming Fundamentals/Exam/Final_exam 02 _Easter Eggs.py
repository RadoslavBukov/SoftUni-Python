"""
Input
@@@@green@*/10/@yel0w@*26*#red#####//8//@limon*@*23*@@@red#*/%^&/6/@gree_een@/notnumber/###purple@@@@@*$%^&*/5/

Output
You found 10 green eggs!
You found 8 red eggs!
You found 6 red eggs!
You found 5 purple eggs!

Input
#@##@red@#/8/@rEd@/2/#@purple@////10/

Output
You found 8 red eggs!
You found 10 purple eggs!
"""
import re
input_text = input()

regex = r"[@#]+(?P<color>[a-z]{3}[a-z]*)[@#]\W*\D*\/(?P<amount>[0-9]+)\/"
matches = re.finditer(regex, input_text)

for match in matches:
    color = match.group("color")
    amount = int(match.group("amount"))
    print(f"You found {amount} {color} eggs!")