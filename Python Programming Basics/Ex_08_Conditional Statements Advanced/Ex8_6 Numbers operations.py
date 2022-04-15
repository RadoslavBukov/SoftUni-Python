"""
Input           Output
10              10 + 12 = 22 - even
12
+
123             123 / 12 = 10.25
12
/
112             Cannot divide 112 by zero
0
/
10              10 - 1 = 9 - odd
1
-
10              10 % 3 = 1
3
%
10              Cannot divide 10 by zero
0
%
7               7 * 3 = 21 - odd
3
*
"""
n1 = int(input())
n2 = int(input())
operation = str(input())

if operation == "+":
    sum = n1+n2
    if sum % 2 ==0:
        ev_od = "even"
    else:
        ev_od = "odd"
    print(f"{n1} {operation} {n2} = {sum} - {ev_od}")
elif operation == "-":
    sum = n1-n2
    if sum % 2 ==0:
        ev_od = "even"
    else:
        ev_od = "odd"
    print(f"{n1} {operation} {n2} = {sum} - {ev_od}")
elif operation == "*":
    sum = n1*n2
    if sum % 2 ==0:
        ev_od = "even"
    else:
        ev_od = "odd"
    print(f"{n1} {operation} {n2} = {sum} - {ev_od}")
elif operation == "/" and n2 != 0:
    sum = n1/n2
    print(f"{n1} {operation} {n2} = {sum:.2f}")
elif operation == "%" and n2 != 0:
    sum = n1+n2
    print(f"{n1} {operation} {n2} = {sum}")
elif (operation == "/" or operation == "%") and n2 == 0:
    print(f"Cannot divide {n1} by zero")