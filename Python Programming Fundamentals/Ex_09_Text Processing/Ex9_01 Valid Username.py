"""
Input	                                                        Output
sh, too_long_username, !lleg@l ch@rs, jeffbutt	                jeffbutt

Jeff, john45, ab, cd, peter-ivanov, @smith	                    Jeff
                                                                John45
                                                                peter-ivanov
"""
import string
text = input().split(", ")
allowed_symbols = string.ascii_letters + string.digits + "-" + "_"

for username in text:
    valid_username = True
    if len(username) < 3 or len(username) > 16:
        valid_username = False
    for latter in username:
        if latter not in allowed_symbols:
            valid_username = False
    if valid_username:
        print(username)