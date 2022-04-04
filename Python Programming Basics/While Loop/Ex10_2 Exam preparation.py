"""
Input               Output
3                   Average score: 5.25
Money               Number of problems: 4
6                   Last problem: Bus
Story
4
Spring Time
5
Bus
6
Enough

2                   You need a break, 2 poor grades.
Income
3
Game Info
6
Best Player
4
"""
poor_grade = int(input())
number_poor_grades = 0
grades_number = 0
grades_sum = 0
task_name = input()

while task_name != "Enough":
    grade = int(input())
    last_task = task_name
    grades_number += 1
    grades_sum += grade
    if grade <= 4:
        number_poor_grades += 1
    if number_poor_grades >= poor_grade:
        print(f"You need a break, {number_poor_grades} poor grades.")
        break
    task_name = input()
if poor_grade > number_poor_grades:
    print(f"Average score: {grades_sum/grades_number:.2f}")
    print(f"Number of problems: {grades_number}")
    print(f"Last problem: {last_task}")