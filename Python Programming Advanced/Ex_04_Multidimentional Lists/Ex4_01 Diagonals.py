"""
Input	        Output
3               Primary diagonal: 1, 5, 9. Sum: 15
1, 2, 3         Secondary diagonal: 3, 5, 7. Sum: 15
4, 5, 6
7, 8, 9
"""
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

primary_diagonal = []
primary_sum = 0
secondary_diagonal = []
secondary_sum = 0

for idx in range(n):
    primary_diagonal.append(matrix[idx][idx])
    primary_sum += matrix[idx][idx]

    secondary_diagonal.append(matrix[idx][n-idx-1])
    secondary_sum += matrix[idx][n-idx-1]

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {secondary_sum}")