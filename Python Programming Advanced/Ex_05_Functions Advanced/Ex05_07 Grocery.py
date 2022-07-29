"""
Test Code	                        Output
print(grocery_store(                pasta: 12
    bread=5,                        eggs: 12
    pasta=12,                       bread: 5
    eggs=12,
))

print(grocery_store(                eggs: 20
    bread=2,                        bread: 2
    pasta=2,                        pasta: 2
    eggs=20,                        carrot: 1
    carrot=1,
))
"""
def grocery_store(**kwargs):
    sorted_store = [f"{key}: {value}" for key, value in sorted(kwargs.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))]
    return "\n".join(sorted_store)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))