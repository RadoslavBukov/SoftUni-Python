"""
Input	                        Output
20, 13, -7, 7                   Great! You filled 2 boxes.
10, 5, 20, 15, 7, 9	            Pieces of paper left: 7, 5, 20, 15

Comment
1) The first egg (20) is wrapped with the last piece of paper (9). We put them in a box and remove them from the sequences.
2) The second egg (13) brings back luck so it's removed. Then the first piece of paper (10) is switched with the last piece of paper (7).
3) The third egg (-7) is not fresh, so we remove it.
4) The fourth egg (7) is wrapped with the last piece of paper (10). We put them in a box and remove them from the sequences. Remove them both.
5) We successfully filled 2 boxes.


Input	                        Output
2, 4, 7, 8, 0                   Great! You filled 3 boxes.
5, 6, 2	                        Eggs left: 8, 0

12, 23                          Sorry! You couldn't fill any boxes!
28, 40
"""
from collections import deque

eggs = deque(map(int, input().split(", ")))
paper_stack = list(map(int, input().split(", ")))

box_size = 50
filled_box = 0

while eggs and paper_stack:
    egg_size = eggs.popleft()
    if egg_size <= 0:
        continue
    if egg_size == 13:
        paper_stack[0], paper_stack[len(paper_stack)-1] = paper_stack[len(paper_stack)-1], paper_stack[0]
        continue

    paper_size = paper_stack.pop()

    if egg_size+paper_size <= box_size:
        filled_box += 1

if filled_box > 0:
    print(f"Great! You filled {filled_box} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: ",end="")
    print(', '.join([str(i) for i in eggs]))
elif paper_stack:
    print(f"Pieces of paper left: ", end="")
    print(', '.join([str(i) for i in paper_stack]))

