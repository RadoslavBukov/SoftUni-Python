"""
Input	                                                    Output
=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=	    Destinations: Hawai, Cyprus
                                                            Travel Points: 11

ThisIs some InvalidInput	                                Destinations:
                                                            Travel Points: 0
"""
import re
location_string = input()
travel_points = 0

regex = r"(?<=([=/]))[A-Z]{1}[A-Za-z]{1}[A-Za-z]+(?=\1)"
matches = re.finditer(regex, location_string)

output = list()
for match in matches:
    output.append(match.group())
    travel_points += len(match.group())

print(f"Destinations: {', '.join(output)}")
print(f"Travel Points: {travel_points}")