"""
Input           Output
10              No more free space! You need 2 Cubic meters more.
10
2
20
20
20
20
122

10              10 Cubic meters left.
1
2
4
6
Done
"""
width = int(input())
length = int(input())
height = int(input())
area = width*length*height

while area > 0:
    boxes = str(input())
    if boxes == "Done":
        print(f"{area} Cubic meters left.")
        break
    else:
        boxes_int = int(boxes)
        area -= boxes_int

if area <= 0:
    print(f"No more free space! You need {abs(area)} Cubic meters more.")
