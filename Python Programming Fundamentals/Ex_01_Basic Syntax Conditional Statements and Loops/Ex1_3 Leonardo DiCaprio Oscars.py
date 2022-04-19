"""
Input	        Output
88	            Leo finally won the Oscar! Leo is happy
86	            Not even for Wolf of Wall Street?!
81	            When will you give Leo an Oscar?
89	            Leo got one already!
"""

number = int(input())

if number == 88 :
    print('Leo finally won the Oscar! Leo is happy')
elif number == 86 :
    print('Not even for Wolf of Wall Street?!')
elif number != 88 and number != 86 and number < 88 :
    print('When will you give Leo an Oscar?')
elif number > 88 :
    print('Leo got one already!')