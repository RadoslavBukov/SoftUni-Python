"""
Input	            Output
30	                30% [%%%.......]
                    Still loading...

50	                50% [%%%%%.....]
                    Still loading...

100	                100% Complete!
                    [%%%%%%%%%%]
"""
def factorial(a):
    fact = 1
    for i in range(a,1,-1):
        fact *= i
    return fact

x = int(input())
y = int(input())
print(f"{factorial(x)//factorial(y):.2f}")
