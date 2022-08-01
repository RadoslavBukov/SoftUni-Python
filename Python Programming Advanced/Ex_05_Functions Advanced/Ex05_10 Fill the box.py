"""
Test Code	                                                    Output	                                                            Comment

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))	    There is free space in the box. You could put 13 more cubes.	    The size of the box: 2 * 8 * 2 = 32
                                                                                                                                    We put the cubes consistently. At the end there is more free space left.

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))	    No more free space! You have 17 more cubes.	                        The size of the box: 5 * 5 * 2 = 50
                                                                                                                                    We put the cubes consistently. First, we put 40 cubes and there is free space left.
                                                                                                                                    Then we try to put 11 cubes, but there is only space for 10.
                                                                                                                                    Cubes left: 1 + 7 + 3 + 1 + 5 = 17

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))	    There is free space in the box. You could put 960 more cubes.
"""
def fill_the_box(height, length, width, *args):
    size = height * length * width
    left_cubes = 0

    for box in args:
        if box == "Finish":
            break
        if box <= size:
            size -= box
        else:
            box -= size
            left_cubes += box
            size = 0

    if size:
        return f"There is free space in the box. You could put {size} more cubes."
    else:
        return f"No more free space! You have {left_cubes} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))