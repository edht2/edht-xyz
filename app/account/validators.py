from string import printable

def validate_signup(first_name: str, last_name:str, email: str, passphrase: str) -> str:

    if len(first_name) > 50:
        return "First name must contain less than 50 characters"

    if len(first_name) < 3:
        return "First name must contain more that 3 characters"

    for char in first_name:
        if !(char in printable):
            return "First Name cannot contain no ASCII characters"

    if len(last_name) > 50:
        return "Last name must contain less than 50 characters"

    if len(last_name) < 3:
        return "Last name must contain more that 3 characters"

    for char in last_name:
        if !(char in printable):
            return "Last Name cannot contain no ASCII characters"
