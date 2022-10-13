"""
Player name: Pall
Points sprint: 1
Points dribble: 3
Points passing: 5
Points shooting: 7

calling the __str__ method
Player: Pall
Sprint: 1
Dribble: 3
Passing: 5
Shooting: 7

About the team
Team name: Best
Teams points: 10
Teams players: 0
Player Pall joined team Best
Player Pall has already joined
Teams players: 1
Player: Pall
Sprint: 1
Dribble: 3
Passing: 5
Shooting: 7
Player Pall not found
"""

from Ex_03_project.player import Player
from Ex_03_project.team import Team


p = Player("Pall", 1, 3, 5, 7)

print("Player name:", p.name)
print("Points sprint:", p._Player__sprint)
print("Points dribble:", p._Player__dribble)
print("Points passing:", p._Player__passing)
print("Points shooting:", p._Player__shooting)

print("\ncalling the __str__ method")
print(p)

print("\nAbout the team")
t = Team("Best", 10)
print("Team name:", t._Team__name)
print("Teams points:", t._Team__rating)
print("Teams players:", len(t._Team__players))
print(t.add_player(p))
print(t.add_player(p))
print("Teams players:", len(t._Team__players))
print(t.remove_player("Pall"))
print(t.remove_player("Pall"))

