"""
Input	                                            Output
print(even_odd_filter(                              {'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(                              {'odd': [5]}
    odd=[2, 2, 30, 44, 10, 5],
))
"""
def even_odd_filter(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == "odd":
            result[key] = []
            for number in value:
                if number % 2 != 0:
                    result[key].append(number)

        elif key == "even":
            result[key] = []
            for number in value:
                if number % 2 == 0:
                    result[key].append(number)

#Variant 2 for "for" cycle:
#   for key, value in kwargs.items():
#       parity = 0 if key == 'even' else 1
#       filtered = [x for x in value if x % 2 == parity]
#       result[key] = filtered

# Sorted by len(value) / for returning dictionary, not tuple -> dict() infront
    return dict(sorted(result.items(), key = lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))