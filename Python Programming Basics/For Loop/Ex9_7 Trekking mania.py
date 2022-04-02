"""
Input               Output
10                  1.84%
10                  6.75%
5                   5.21%
1                   31.60%
100                 54.60%
12
26
17
37
40
78

5                   0.00%
25                  1.70%
41                  7.08%
31                  8.78%
250                 82.44%
6
"""
group = int(input())
all_people=0
Musala=0
MontBlanc=0
Kilimanjaro=0
K2=0
Everest=0

for i in range(0, group):
    number_people = int(input())
    if number_people <= 5:
        Musala += number_people
    elif 5 < number_people <= 12:
        MontBlanc += number_people
    elif 12 < number_people <= 25:
        Kilimanjaro += number_people
    elif 25 < number_people <= 40:
        K2 += number_people
    elif number_people > 40:
        Everest += number_people
    all_people += number_people

Musala_percent = Musala/all_people*100
MontBlanc_percent = MontBlanc/all_people*100
Kilimanjaro_percent = Kilimanjaro/all_people*100
K2_percent = K2/all_people*100
Everest_percent = Everest/all_people*100

print(f"{Musala_percent:.2f}%")
print(f"{MontBlanc_percent:.2f}%")
print(f"{Kilimanjaro_percent:.2f}%")
print(f"{K2_percent:.2f}%")
print(f"{Everest_percent:.2f}%")