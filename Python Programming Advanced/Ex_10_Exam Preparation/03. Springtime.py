"""
Test Code                                                   Output
-{last_spring_object_of_typeN}"                             flower:
Examples                                                    -Dahlia
Test Code	Output                                          -Tulip
example_objects = {"Water Lilly": "flower",                 -Water Lilly
                   "Swifts": "bird",                        bird:
                   "Callery Pear": "tree",                  -Swallows
                   "Swallows": "bird",                      -Swifts
                   "Dahlia": "flower",                      tree:
                   "Tulip": "flower",}                      -Callery Pear
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",                       bird:
                   "Thrushes": "bird",                      -Shrikes
                   "Woodpeckers": "bird",                   -Swallow
                   "Swallows": "bird",                      -Swallows
                   "Warblers": "bird",                      -Thrushes
                   "Shrikes": "bird",}                      -Warblers
print(start_spring(**example_objects))	                    -Woodpeckers

example_objects = {"Magnolia": "tree",                      bird:
                   "Swallow": "bird",                       -Shrikes
                   "Thrushes": "bird",                      -Swallow
                   "Pear": "tree",                          -Thrushes
                   "Cherries": "tree",                      tree:
                   "Shrikes": "bird",                       -Cherries
                   "Butterfly": "insect"}                   -Magnolia
print(start_spring(**example_objects))	                    -Pear
                                                            insect:
                                                            -Butterfly
"""
def start_spring(**kwargs):
    items = {}
    for key, value in kwargs.items():
        if value not in items:
            items[value] = []
        items[value].append(key)

    sorted_items = sorted(items.items(), key = lambda x: (-len(x[1]), x[0]))

    result = []

    for key, value in sorted_items:
        result.append(f"{key}:")
        for el in sorted(value):
            result.append(f"-{el}")

    return "\n".join(result)

    # result = {}
    #
    # for spring_object, names in sorted_items:
    #     if spring_object not in result:
    #         result[spring_object] = sorted(names)
    #
    # for (key, value) in result.items():
    #     print(f"{key}:")
    #     for names in (value):
    #         print(f"- {names}")

# Test Code 1
example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))

# Test Code 2
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

# Test Code 3
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))
