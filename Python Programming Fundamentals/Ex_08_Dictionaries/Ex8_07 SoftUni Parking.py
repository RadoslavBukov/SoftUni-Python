"""
Input	                                        Output
5                                               John registered CS1234JS successfully
register John CS1234JS                          George registered JAVA123S successfully
register George JAVA123S                        Andy registered AB4142CD successfully
register Andy AB4142CD                          Jesica registered VR1223EE successfully
register Jesica VR1223EE                        Andy unregistered successfully
unregister Andy	                                John => CS1234JS
                                                George => JAVA123S
                                                Jesica => VR1223EE
4
register Jony AA4132BB                          Jony registered AA4132BB successfully
register Jony AA4132BB                          ERROR: already registered with plate number AA4132BB
register Linda AA9999BB                         Linda registered AA9999BB successfully
unregister Jony	                                Jony unregistered successfully
                                                Linda => AA9999BB
6
register Jacob MM1111XX                         Jacob registered MM1111XX successfully
register Anthony AB1111XX                       Anthony registered AB1111XX successfully
unregister Jacob                                Jacob unregistered successfully
register Joshua DD1111XX                        Joshua registered DD1111XX successfully
unregister Lily                                 ERROR: user Lily not found
register Samantha AA9999BB	                    Samantha registered AA9999BB successfully
                                                Anthony => AB1111XX
                                                Joshua => DD1111XX
                                                Samantha => AA9999BB
"""
number = int(input())
parking = dict()

for i in range(0, number):
    text = input().split(" ")
    if text[0] == "register":
        username = text[1]
        plate_number = text[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            parking[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    elif text[0] == "unregister":
        username = text[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del[parking[username]]
            print(f"{username} unregistered successfully")

for (key,value) in parking.items():
    print(f"{key} => {(value)}")