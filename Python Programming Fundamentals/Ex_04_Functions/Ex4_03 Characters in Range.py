"""
Input	        Output
a               b c
d

#               $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9
:

#               $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
C
"""
def string_print(a,b):
    for i in range (ord(a)+1,ord(b)):
        print(chr(i),end=" ")

x,y = str(input()), str(input())

string_print(x,y)