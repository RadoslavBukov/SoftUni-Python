"""
Input	                    Output

abc@abv.bg	                Traceback (most recent call last):
                               File ".\email_validator.py", line 20, in <module>
                                raise NameTooShort("Name must be more than 4 characters")
                            __main__.NameTooShort: Name must be more than 4 characters

peter@gmail.com             Email is valid
petergmail.com              Traceback (most recent call last):
                              File ".\email_validator.py", line 18, in <module>
                                raise MustContainAtSymbolError("Email must contain @")
                            __main__.MustContainAtSymbolError: Email must contain @

peter@gmail.hotmail	        Traceback (most recent call last):
                              File ".\email_validator.py", line 22, in <module>
                                raise InvalidDomainError("Domain must be one of the folowing: .com, .bg, .org, .net")
                            __main__.InvalidDomainError: Domain must be one of the folowing: .com, .bg, .org, .net
"""
from custom_exeptions import MustContainAtSymbolError, NameTooShortError, InvalidDomainError

valid_domains = {".com", ".bg", ".org", ".net"}

while True:
    input_line = input()
    if input_line == "End":
        break

    email = input_line
    email_parts = email.split("@")

    if len(email_parts) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_name = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = f".{domain_name.split('.')[-1]}"

    if domain not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    print("Email is valid")