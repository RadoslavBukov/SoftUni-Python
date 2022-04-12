"""
Input               Output
Taxi                Taxi - 60.00% full.
10                  Scary Movie - 100.00% full.
standard            Total tickets: 12
kid                 66.67% student tickets.
student             25.00% standard tickets.
student             8.33% kids tickets.
standard
standard
End
Scary Movie
6
student
student
student
student
student
student
Finish

The Matrix          The Matrix - 40.00% full.
20                  The Green Mile - 35.29% full.
student             Amadeus - 100.00% full.
standard            Total tickets: 17
kid                 41.18% student tickets.
kid                 47.06% standard tickets.
student             11.76% kids tickets.
student
standard
student
End
The Green Mile
17
student
standard
standard
student
standard
student
End
Amadeus
3
standard
standard
standard
Finish
"""
movie_name = (input())
standard = 0
student = 0
kid = 0
number = 0

while movie_name != "Finish":
    free_seats = int(input())
    total_number = 0
    for i in range (1, free_seats+1):
        ticket_type = str(input())
        if ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kid += 1
        elif ticket_type == "student":
            student += 1
        elif ticket_type == "End":
            break
        total_number += 1
    number += total_number
    print(f"{movie_name} - {(total_number/free_seats)*100:.2f}% full.")
    movie_name = str(input())
print(f"Total tickets: {number}")
print(f"{(student/number)*100:.2f}% student tickets.")
print(f"{(standard/number)*100:.2f}% standard tickets.")
print(f"{(kid/number)*100:.2f}% kids tickets.")