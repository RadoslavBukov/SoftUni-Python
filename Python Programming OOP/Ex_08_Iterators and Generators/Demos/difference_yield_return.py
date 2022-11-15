def gen_func(n):
    print('The start')
    for x in range(n):
        yield x


def norm_func(n):
    for x in range(n):
        return x


print(norm_func(5))
gf = gen_func(5)
print(gf) # calling gen_func returns generator object
print(next(gf)) # calling 'next' of gen_func start execute the gen_func till the 'yield'
print(next(gf)) # next 'next' calling of the gen_func resume executing the funk from the last 'yield' to the next 'yield'
