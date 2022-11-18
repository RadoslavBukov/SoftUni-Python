"""
Test Code	                                                Output

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))	        [2, 3, 5]
print(list(get_primes([-2, 0, 0, 1, 1, 0])))	            []
"""
def is_prime(number):
    if number <= 1:
        return False

    prime = True
    for i in range(2, number):
        if number % i ==0:
            prime = False
            break
    return prime

def get_primes(list):
    for number in list:
        if is_prime(number):
            yield number


# Test Code 1
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# Test Code 2
print(list(get_primes([-2, 0, 0, 1, 1, 0])))

