"""
Input       Output                              Input       Output
5           Final points: 8040                  4           Final points: 6190
1400        Average points: 1328                750         Average points: 1360
F           40.00%	                            SF          50.00%
SF                                              W
W                                               SF
W                                               W
SF

7           Final points: 11040
1200        Average points: 1405
SF          42.86%
F
W
F
W
SF
W
"""
import math
tournaments = int(input())
points = int(input())
winned_points=0
winned_tournaments=0

for i in range(0, tournaments):
    ranking = str(input())
    if ranking == "W":
        winned_points += 2000
        winned_tournaments += 1
    elif ranking == "F":
        winned_points += 1200
    elif ranking == "SF":
        winned_points += 720

points += winned_points
print(f"Final points: {points}")
print(f"Average points: {math.floor(winned_points/tournaments)}")
print(f"{(winned_tournaments/tournaments)*100:.2f}%")