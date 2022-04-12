"""
Input                   Output
2                       While-Loop - 5.75.
While-Loop              For-Loop - 5.75.
6.00                    Student's final assessment is 5.75.
5.50
For-Loop
5.84
5.66
Finish

3                       Arrays - 4.92.
Arrays                  Lists - 5.75.
4.53                    Student's final assessment is 5.34.
5.23
5.00
Lists
5.83
6.00
5.42
Finish

2                       Objects and Classes - 5.00.
Objects and Classes     Dictionaries - 4.82.
5.77                    RegEx - 3.15.
4.23                    Student's final assessment is 4.32.
Dictionaries
4.62
5.02
RegEx
2.88
3.42
Finish
"""
n = int(input())
presentation_name = str(input())
average_grades = 0
grades_number = 0

while presentation_name != "Finish":
    grades_sum = 0
    for i in range (1, n+1):
        grade = float(input())
        grades_sum += grade
        grades_number += 1
    print(f"{presentation_name} - {grades_sum/n:.2f}.")
    average_grades += grades_sum
    presentation_name = str(input())
print(f"Student's final assessment is {average_grades/grades_number:.2f}.")