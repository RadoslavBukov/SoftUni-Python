"""
Test Code	                                                    Output
print(even_odd(1, 2, 3, 4, 5, 6, "even"))	                    [2, 4, 6]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))	        [1, 3, 5, 7, 9]
"""
def even_odd(*args):
    command = args[-1]
    numbers = []
    for idx in range(len(args)-1):
        if command == "even":
            if args[idx] % 2 == 0:
                numbers.append(args[idx])
        elif command == "odd":
            if args[idx] % 2 != 0:
                numbers.append(args[idx])
    return numbers

print(even_odd(1, 2, 3, 4, 5, 6, "even"))

"""
#Variant 2

def even_odd(*args):
    filter_command = args[-1]
    parity = 0 if filter_command == 'even' else 1
    result = []
    for idx in range(len(args)-1):
        number = args[idx]
        if number % 2 == parity:
            result.append(args[idx])
    return result

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
"""