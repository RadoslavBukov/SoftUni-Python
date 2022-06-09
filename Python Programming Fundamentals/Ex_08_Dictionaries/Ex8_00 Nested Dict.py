"""
Input                                   Output
Peter:123:programming basics            John - 5622
John:5622:fundamentals                  Maya - 89
Maya:89:fundamentals                    Lilly - 633
Lilly:633:fundamentals
fundamentals
"""
text = input()
courses = dict()

while ":" in text:

    data = text.split(":")
    name = data[0]
    id = data[1]
    course = data[2]
#   name, id, course = data[0], data[1], data[2]
#   (name, id, course) = text.split(":") - text in typle

    if course not in courses.keys():
        courses[course] = dict()

    courses[course][id] = name

    text = input()

text = text.replace("_"," ")

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")
