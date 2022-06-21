"""
Input	                                                                                                                                    Output
Please contact us at: support@github.com.	                                                                                                support@github.com
Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.	                                                        s.miller@mit.edu
j.hopking@york.ac.uk
Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de.	steve.parker@softuni.de
"""

# Variant 1
import re
text = input()

expression = r"(^| )[A-Za-z0-9]+([._-][A-Za-z0-9]+)*[@][A-Za-z]+(-[A-Za-z]+)*(\.[A-Za-z]+)+"
# Working       r"( |^)[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*[@][a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"

"""
#Variant 2:
user_pattern = r"(^| )[A-Za-z0-9]+([._-][A-Za-z0-9]+)*"
host_pattern = r"[A-Za-z]+(-[A-Za-z]+)*(\.[A-Za-z]+)+"
expression = rf"{user_pattern}@{host_pattern}"
"""
matches = re.finditer(expression, text)

output = list()
for match in matches:
    output.append(match.group())

print("\n".join(output))

"""
# Variant 3
import re
text = input()

user_pattern = r"( |^)[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*"
host_pattern = r"[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"
pattern = rf"{user_pattern}@{host_pattern}"

emails = re.finditer(pattern, text)

for email in emails:
    print(email[0])
"""