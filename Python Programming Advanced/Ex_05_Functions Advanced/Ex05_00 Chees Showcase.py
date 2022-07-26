"""
White a function called sorting_cheeses that receives keywords arguments:
•	The key represents the name of the cheese
•	The value is a list of quantities (integers) of the pieces of the given cheese
The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in descending order.
If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically).
For each kind of cheese, return their pieces quantities in descending order.
"""
import os

def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(
        kwargs.items(),
# the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in descending order : (-len[x1]) - x1 = value
# If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically) : x[0] = key = name
        key=lambda x: (-len(x[1]), x[0]),
    )

    result = []

    for name, pieces_counts in sorted_cheeses:
        result.append(name)
# For each kind of cheese, return their pieces quantities in descending order: piece_counts, reverse=True
        result.extend(
            sorted(pieces_counts, reverse=True)
        )

        # '\n' don't use this!
        # '\n\r' for Windows
        # os.linesep
    return '\n'.join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)