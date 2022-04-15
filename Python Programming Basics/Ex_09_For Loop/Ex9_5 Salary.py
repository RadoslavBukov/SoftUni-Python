"""
Input                   Output
10                      You have lost your salary.
750
Facebook
Dev.bg
Instagram
Facebook
Reddit
Facebook
Facebook

3                       500
500
Github.com
Stackoverflow.com
softuni.bg

3                       350
500
Facebook
Stackoverflow.com
softuni.bg
"""
n = int(input())
salary = int(input())
penalty=0

for i in range(0, n):
    text = str(input())
    if text == "Facebook":
        penalty += 150
    elif text == "Instagram":
        penalty += 100
    elif text == "Reddit":
        penalty += 50

if salary - penalty <= 0:
    print(f"You have lost your salary.")
else:
    print(salary-penalty)