"""
Input	            Output
logIn	            Password must be between 6 and 10 characters
                    Password must have at least 2 digits

MyPass123	        Password is valid

Pa$s$s	            Password must consist only of letters and digits
                    Password must have at least 2 digits
"""
def passwd_check(passwd):
    _return_val = True
    special_symbol = list()
    for i in range(31, 128):
        if (31 < i < 48) or (57 < i < 65) or (90 < i < 97) or (122 < i < 128):
            special_symbol.append(chr(i))
#    numbers = sum(c.isdigit() for c in passwd)                          # Numbers of digits
#    letters = sum(c.isalpha() for c in passwd)                          # Number of letters
#    special_symbols = len(passwd) - numbers - letters                   # number of special symbols
    if len(passwd) < 6 or len(passwd) > 10:
        print('Password must be between 6 and 10 characters')
        _return_val = False
    if any(char in special_symbol for char in passwd):
        print('Password must consist only of letters and digits')
        _return_val = False
    if sum(d.isdigit() for d in passwd) < 2:
         print('Password must have at least 2 digits')
         _return_val = False
    if not any(char.islower() for char in passwd):
        print('the password should have at least one lowercase letter')
        _return_val = False
    if _return_val:
        print('Password is valid')

a = str(input())
passwd_check(a)