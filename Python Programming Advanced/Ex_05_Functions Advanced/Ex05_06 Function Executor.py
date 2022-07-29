"""
Test Code	                                                        Output
def sum_numbers(num1, num2):                                        sum_numbers - 3
    return num1 + num2                                              multiply_numbers - 8

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))

def make_upper(*strings):                                           make_upper - ('PYTHON', 'SOFTUNI')
    result = tuple(s.upper() for s in strings)                      make_lower - ('python', )
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
"""
def func_executor(*args):
    result = []
    for function_name, function_param in args:
        function_result = function_name(*function_param)
        result.append(f"{function_name.__name__} - {function_result}")
    return "\n".join(result)

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
