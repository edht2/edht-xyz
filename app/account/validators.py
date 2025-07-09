from string import ascii_uppercase, ascii_lowercase
from email_validator import validate_email

chars_whitelist = [chr(i) for i in range(32, 126)]
# All allowed characters for names

def validate_name(name: str) -> str:

    if len(name) >= 50:
        return "Names cannot contain more than 50 characters"

    if len(name) < 3:
        return "Names cannot be less than 3 characters"

    for c in name:
        if not c in chars_whitelist:
            # if a character is not in the allowed chars
            return "Names can only include ASCII characters (32 to 126)"

    return "passed"


def validate_email(email: str) -> str:
    # Just a quick and simple validation that the email is correctly formatted
    try:
        # validate_email(email, check_deliverability=False)
        return "passed"

    except:
        return "Email is invalid"


def validate_signup(first_name: str, last_name: str, email: str) -> dict:
    # Starting with 'first_name' and 'last_name'
    first_name_results = validate_name(first_name)
    last_name_results = validate_name(last_name)

    name_results = first_name_results
    if first_name_results == "passed":
        name_results = last_name_results

    # Finally 'email'
    email_results = validate_email(email)

    # Summary (for neater code later)
    summary = False
    if (name_results != "passed" or email_results != "passed"):
        summary = True

    return {
        "name_results" : name_results,
        "email_results" : email_results,
        "summary" : summary
    }





