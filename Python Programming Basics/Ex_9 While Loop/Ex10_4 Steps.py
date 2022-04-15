"""
Input       Output                                  Input           Output
1000        Goal reached! Good job!                 1500            2500 more steps to reach goal.
1500        1000 steps over the goal!               300
2000                                                2500
6500                                                3000
                                                    Going home
                                                    200

1500        Goal reached! Good job!                 125             Goal reached! Good job!
3000        298 steps over the goal!                250             1765 steps over the goal!
250                                                 4000
1548                                                30
2000                                                2678
Going home                                          4682
2000
"""
steps_per_day = ""
steps_per_day_int = 0
all_steps = 0

while all_steps < 10000:
    steps_per_day = str(input())
    if steps_per_day == "Going home":
        steps_home = int(input())
        all_steps += steps_home
        if all_steps < 10000:
            print(f"{10000 - all_steps} more steps to reach goal.")
        break
    steps_per_day_int = int(steps_per_day)
    all_steps += steps_per_day_int

if all_steps >= 10000:
    print(f"Goal reached! Good job!")
    if all_steps > 1000:
        print(f"{all_steps-10000} steps over the goal!")