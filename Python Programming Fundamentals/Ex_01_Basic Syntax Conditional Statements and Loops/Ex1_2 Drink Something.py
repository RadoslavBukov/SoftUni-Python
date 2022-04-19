"""
Input   	Output
13	        drink toddy
17	        drink coke
21	        drink beer
30	        drink whisky
"""

age = int(input())

if age <= 14 :
    print('drink toddy')
elif 14 < age <= 18:
    print('drink coke')
elif 18 < age <= 21:
    print('drink beer')
elif age > 21:
    print('drink whisky')