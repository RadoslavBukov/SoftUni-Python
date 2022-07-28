"""
Test Code	                                        Output
dictionary = {'name': 'Peter', 'age': 25}           2
print(kwargs_length(**dictionary))

dictionary = {}                                     0
print(kwargs_length(**dictionary))
"""
def kwargs_length(**kwargs):
    return len(kwargs)

dictionary = {'name': 'Peter', 'age': 25 , 'sex': ' m'}

print(kwargs_length(**dictionary))