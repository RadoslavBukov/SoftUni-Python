"""
George Peter Michael William Thomas         (every 3rd)
  1      2      3                           #Michael is out
George Peter William Thomas
  3             1       2                   #George is out
Peter William Thomas
  1      2      3                           # Thomas is out
Peter William
  1      2
  3                                         # Peter is out
William                                     # William left last - is a winner

############
Input                                       Output
George Peter Michael William Thomas         Removed Thomas
10                                          Removed Peter
                                            Removed Michael
                                            Removed George
                                            Last is William
"""
from collections import deque

kids_string = input()
tosses_count = int(input())

kids = deque(kids_string.split())

current_count = 0
while len(kids) > 1:
    current_count += 1
    kid = kids.popleft()
    if current_count < tosses_count:
        kids.append(kid)
    else:
        print(f"Removed {kid}")
        current_count = 0

print(f"Last is {kids.popleft()}")