"""
Input
+359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222

Output
+359 2 222 2222, +359-2-222-2222
"""
import re
phone_numbers = input()

# Variant 1
matches = re.findall(r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b", phone_numbers)  # we are looking for numbers with space or "-" between
print(", ".join(matches))

"""
# Variant 2 - when there are groups in regex () - then we should use finditer, matches is no longer list, so we should print it otherway:
matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", phone_numbers)

for match in matches:
    print(match.group())
"""