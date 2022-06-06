"""
Input	                                            Output
Programming Fundamentals : John Smith               Programming Fundamentals: 2
Programming Fundamentals : Linda Johnson            -- John Smith
JS Core : Will Wilson                               -- Linda Johnson
Java Advanced : Harrison White                      JS Core: 1
end	Programming Fundamentals: 2                     -- Will Wilson
                                                    Java Advanced: 1
                                                    -- Harrison White

Algorithms : Jay Moore                              Algorithms: 2
Programming Basics : Martin Taylor                  -- Jay Moore
Python Fundamentals : John Anderson                 -- Bob Jackson
Python Fundamentals : Andrew Robinson               Programming Basics: 1
Algorithms : Bob Jackson                            -- Martin Taylor
Python Fundamentals : Clark Lewis                   Python Fundamentals: 3
end	                                                -- John Anderson
                                                    -- Andrew Robinson
                                                    -- Clark Lewis
"""
text = input().split(" : ")
courses = dict()

while text[0] != "end":

    course = text[0]
    name = text[1]
    if course not in courses.keys():
        courses[course] = list()

    courses[course].append(name)

    text = input().split(" : ")

for (key, value) in courses.items():
    print(f"{key}: {len(value)}")
    for names in (value):
        print(f"-- {names}")