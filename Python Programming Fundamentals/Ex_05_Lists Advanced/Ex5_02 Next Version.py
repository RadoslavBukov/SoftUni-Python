"""
Input	    Output
1.2.3	    1.2.4

1.3.9	    1.4.0

3.9.9	    4.0.0
"""
input_version = input().split(".")
int_version = int("".join(input_version))
int_version += 1;

new_version = [x for x in str(int_version)]

print(f"{'.'.join(new_version)}")

"""
def next_version(version_number):
    version_number = int(''.join(version_number))+1
    result = [str(num) for num in str(version_number)]
    print('.'.join(result))
     
data = input().split('.') 
next_version(data)
"""