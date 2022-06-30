"""
Input	            Output
{[()]}	            YES
{[(])}	            NO
{{[[(())]]}}	    YES
"""
sequence_of_parentheses = input()
opening_brackets = []
balanced = True
"""
#Variant 2: using dictionaries
pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
}
# same => pairs = {'(': ')', '[': ']', '{': '}'}
+ row 29
"""
for ch in sequence_of_parentheses:
    if ch in '({[':
        opening_brackets.append(ch)
    elif ch in ')}]':
        if not opening_brackets:
            balanced = False
            break
        last_opening_bracket = opening_brackets.pop()
        if (last_opening_bracket != "(" and ch == ")") or (last_opening_bracket != "[" and ch == "]") or (last_opening_bracket != "{" and ch == "}"):
#       if pairs[last_opening_bracket] != ch:
            balanced = False
            break
if balanced and not opening_brackets:
    print("YES")
else:
    print("NO")