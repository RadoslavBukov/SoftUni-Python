"""
Input       Output                              Input       Output
9           Late                                9           Late
30          20 minutes after the start          00          1:30 hours after the start
9                                               10
50	                                            30

10          On time                             9           On time
00                                              00          30 minutes before the start
10                                              8
00                                              30

14          On time                             11          Early
00          5 minutes before the start          30          35 minutes before the start
13                                              10
55	                                            55

16          Early                               11          Early
00          1:00 hours before the start         30          3:18 hours before the start
15                                              8
00	                                            12

11          Late
30          59 minutes after the start
12
29
"""
exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

if exam_hour == 0:
    exam_hour = 24
elif arrival_hour == 0:
    arrival_hour = 24

all_exam_min = exam_min + (exam_hour*60)
all_arival_min = arrival_min + (arrival_hour*60)

if all_arival_min > all_exam_min:
    print("Late")
    if all_arival_min - all_exam_min < 60:
        print(f"{all_arival_min-all_exam_min} minutes after the start")
    else:
        late_hour = (all_arival_min - all_exam_min) // 60
        late_min = (all_arival_min - all_exam_min) % 60
        if late_min <= 9:
            print (f"{late_hour}:0{late_min} hours after the start")
        else:
            print(f"{late_hour}:{late_min} hours after the start")
elif all_exam_min >= all_arival_min:
    if all_exam_min-all_arival_min <= 30:
        print("On time")
        if all_exam_min-all_arival_min != 0:
            print(f"{all_exam_min-all_arival_min} minutes before the start")
    elif 30 < all_exam_min-all_arival_min < 60:
        print("Early")
        print(f"{all_exam_min - all_arival_min} minutes before the start")
    elif all_exam_min-all_arival_min >= 60:
        print("Early")
        late_hour = (all_exam_min - all_arival_min) // 60
        late_min = (all_exam_min - all_arival_min) % 60
        if late_min <= 9:
            print(f"{late_hour}:0{late_min} hours before the start")
        else:
            print(f"{late_hour}:{late_min} hours before the start")