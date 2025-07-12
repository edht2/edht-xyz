from app.extensions import db
from app.models.account import Account

chars_whitelist = [chr(i) for i in range(32, 126)]
# All allowed characters for names

def validate_name(name: str) -> str:
    """ Validates the name of the user (first name and surname)
    Requirements: name must have a number of chars between 3 and 50, name must contain ASCII chars between 32 and 126 """
    
    if not name:
        return 'You must include both names'

    if len(name) >= 50:
        return "Names cannot contain more than 50 characters"

    if len(name) < 3:
        return "Names cannot be less than 3 characters"

    for c in name:
        if not c in chars_whitelist:
            # if a character is not in the allowed chars
            return "Names can only include ASCII characters (32 to 126)"

    return ''

def validate_email(email: str) -> str:
    """ Validate the email input; check it contains a name, '@', domain, '.' and tail
    There are many more things that an email must contain / not contain, however just a basic test is necessary here """
    
    if not email:
        # if the user didn't enter an email
        return 'You include an email'
    
    if db.session.query(Account).filter_by(email=email).first():
        # if the email is already connected to an account
        return 'Email is already in use'
            
    if not '@' in email or not '.' in email:
        # if the email doesn't contain '@' or '.' there is a problem
        return "Email is invalid"
    
    return ''

def validate_passphrase(passphrase: str) -> str:
    """ Validates passphrase
    Requirements: must be more than 3 chars """
    
    if not passphrase:
        return 'You must include a passphrase (password)'
    
    if len(passphrase) < 3:
        return 'Passphrase must contain more than 3 characters'
    
    return ''

def validate_signup(first_name: str, last_name: str, email: str, passphrase: str) -> dict:
    # Starting with 'first_name' and 'last_name'
    first_name_results = validate_name(first_name)
    last_name_results = validate_name(last_name)

    name_results = first_name_results
    if not first_name_results:
        name_results = last_name_results

    # Then 'email'
    email_results = validate_email(email)
    
    # Finally 'passphrase'
    passphrase_results = validate_passphrase(passphrase)

    # Summary (for neater code later)
    summary = False
    if name_results or email_results or passphrase_results:
        # if any of the results were invalid
        summary = True

    return {
        "name_results" : name_results,
        "email_results" : email_results,
        "passphrase_results" : passphrase_results,
        "summary" : summary
    }





