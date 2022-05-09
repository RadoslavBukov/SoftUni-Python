"""
Input	            Output
60                  < = > ? @ A
65

69                  E F G H I J K L M N O
79

97                  a b c d e f g h
104
"""

start_symbol = int(input())
stop_sumbol = int(input())

for i in range(start_symbol, stop_sumbol+1):
    print(chr(i),end=' ')