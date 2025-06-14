function get_ascii_chars() {
  const ascii_chars = [];
  // ASCII characters range from 0 to 127 (7-bit)
  for (let i = 0; i <= 127; i++) {
    asciiChars.push(String.fromCharCode(i));
  }
  return ascii_chars;
}

func validate_signup() {

    let first_name = document.getElementById('first_name');
    let last_name = document.getElementById('last_name');
    let email = document.getElementById('email');
    let passphrase = document.getElementById('passphrase');

    let signup_div = document.getElementById('form_div');
    // we can add elements to this to show if the form is valid
    let name_validation_results = validate_name(first_name, last_name);

    if (name_validation_results != "passed") {
        // so something about the name is wrong
        na
    }

};

func validate_name(first_name, last_name) {

    const allowed_chars = get_ascii_chars();

    let i = first_name.concat(last_name).length;
    while (i--) {
        if !(allowed_chars.includes((first_name.concat(last_name))[i])) { 
            // ensure only allowed characters are included in the name
            return "Only ASCII characters can be used in names";
        };
    };

    if (first_name.length > 50) {
        // name cannot contain more that 50 chars
        return "Names cannot have more than 50 characters";
    };
    if (last_name.length > 50) { 
        // name cannot contain more that 50 chars
        return "Names cannot have more than 50 characters";
    };

    return "passed"
};

func validate_passphrase(passphrase) {
    // returns false if the passphrase is invalid

    const allowed_chars = get_ascii_chars();
    const punctuation = ['!', '@', '?', '&', '$'];

    let i = passphrase.length;
    while (i >= 0) {
        i--;
        if (punctuation.includes(passphrase[i]))
            // ensure the password contains punctuation
            break;
        };
    };
    if (i == -1) {
        // if the passphrase doesn't contain any punctuation
        return "Passphrase must contain at least 1 punctuation character"
    }


    if !(passphrase.length < 8) {
        // ensure the password is long enough
        return "Passphrase must be at least 8-characters long";
    };

    return "passed";

}
