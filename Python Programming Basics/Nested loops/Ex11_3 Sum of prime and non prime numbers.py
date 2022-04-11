"""
Input       Output                                      Input       Output
3           Sum of all prime numbers is: 29             30          Number is negative.
9           Sum of all non prime numbers is: 13         83          Sum of all prime numbers is: 83
0                                                       33          Sum of all non prime numbers is: 83
7                                                       -1
19                                                      20
4                                                       stop
stop

0           Number is negative.
-9          Sum of all prime numbers is: 0
0           Sum of all non prime numbers is: 13
stop
"""
number_str = str(input())
suma_prime = 0
suma_nonprime = 0

while number_str != "stop":
    number = int(number_str)
    if number < 0:
        print("Number is negative.")
    else:
        divider = 0
        for i in range (1, number+1):
            if number % i == 0:
                divider += 1
        if divider == 2:
            suma_prime += number
        else:
            suma_nonprime += number
    number_str = str(input())
print(f"Sum of all prime numbers is: {suma_prime}")
print(f"Sum of all non prime numbers is: {suma_nonprime}")