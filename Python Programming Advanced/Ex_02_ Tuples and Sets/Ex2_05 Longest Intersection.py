"""
Input	        Output	                                                            Comment
3               Longest intersection is [6, 7, 8, 9, 10] with length 5              The intersection of [0-3] and [1-2] is [1-2] (length 2)
0,3-1,2                                                                             The intersection of [2-10] and [3-5] is [3-5] (length 3)
2,10-3,5                                                                            The intersection of [6-15] and [3-10] is [6-10] (length 5) - which is the longest
6,15-3,10

5
0,10-2,5        Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11
"""
n = int(input())
longest_intersection = set()

for _ in range(n):
    first_set = set()
    second_set = set()
    ranges = input().split("-")
    first_start, first_end = ranges[0].split(",")
    second_start, second_end = ranges[1].split(",")
# For taking first_start, first_end, second_start, second_end as int:
#   first_start, first_end = [int(x) for x in first_set.split(", ")]
#   second_start, second_end = [int(x) for x in second_set.split(", ")]
    for num in range(int(first_start), int(first_end)+1):
        first_set.add(num)
# The for cycles can be replaced by:
#   first_set = set(range(first_start, first_end + 1))
    for num2 in range(int(second_start), int(second_end)+1):
        second_set.add(num2)
#   second_set = set(range(second_start, second_end + 1))
    if len(first_set&second_set) > len(longest_intersection):
        longest_intersection = first_set&second_set

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")