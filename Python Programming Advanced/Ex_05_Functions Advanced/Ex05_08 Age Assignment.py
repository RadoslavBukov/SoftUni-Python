"""
Test Code	                                                            Output
print(age_assignment("Peter", "George", G=26, P=19))	                George is 26 years old.
                                                                        Peter is 19 years old.

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))	        Amy is 22 years old.
                                                                        Bill is 61 years old.
                                                                        Willy is 36 years old.
"""
def age_assignment(*args, **kwargs):
    result = {}
    for key, value in kwargs.items():
        for name in args:
            if name[0] == key:
                result[name] = value
    sorted_result = [f"{key} is {value} years old." for key, value in sorted(result.items(), key = lambda x: x[0])]
    return '\n'.join(sorted_result)

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))