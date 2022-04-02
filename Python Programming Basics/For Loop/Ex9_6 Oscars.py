"""
Input                   Output
Zahari Baharov          Sorry, Zahari Baharov you need 247.5 more!
205
4
Johnny Depp
45
Will Smith
29
Jet Lee
10
Matthew Mcconaughey
39

Sandra Bullock          Congratulations, Sandra Bullock got a nominee for leading role with 1268.5!
340
5
Robert De Niro
50
Julia Roberts
40.5
Daniel Day-Lewis
39.4
Nicolas Cage
29.9
Stoyanka Mutafova
33
"""
actor_name = str(input())
academy_points = float(input())
number_judge = int(input())

for i in range(0, number_judge):
    judge_name = str(input())
    rating = float(input())
    letter_number = len(judge_name)
    if academy_points <= 1250.5:
        academy_points = academy_points + ((letter_number*rating) / 2)

if academy_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5-academy_points:.1f} more!")