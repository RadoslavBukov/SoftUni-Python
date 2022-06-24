"""
Input                                                   Output

4                                                       Request: Isi
$Request$: [73]|[115]|[105]|                            Valid message not found!
%Taggy$: [73]|[73]|[73]|                                Taggy: val
%Taggy%: [118]|[97]|[108]|                              Valid message not found!
$Request$: [73]|[115]|[105]|[32]|[75]|

3                                                       Valid message not found!
This shouldnt be valid%Taggy%: [118]|[97]|[108]|        Valid message not found!
$tAGged$: [97][97][97]|                                 Valid message not found!
$Request$: [73]|[115]|[105]|true

"""
import re
input_number = int(input())
is_valid = False

for i in range(input_number):
    message = input()
    regex = r"(^|(?<=\s))([$%])(?P<tag>[A-Z][a-z]{2}[a-z]*)\2:\s(\[(?P<Number1>[0-9]+)\]\|)(\[(?P<Number2>[0-9]+)\]\|)(\[(?P<Number3>[0-9]+)\]\|)($|(?=\s))"
    matches = re.finditer(regex, message)

    is_valid = bool(re.search(regex, message))

    if is_valid:
        for match in matches:
            tag = match.group("tag")
            number1 = int(match.group("Number1"))
            number2 = int(match.group("Number2"))
            number3 = int(match.group("Number3"))
            print(f"{tag}: {chr(number1)}{chr(number2)}{chr(number3)}")
    else:
        print("Valid message not found!")