def is_email(text):
    """Pārbauda, vai teksts satur @ un . simbolus."""
    return "@" in text and "." in text

def is_phone_number(text):
    """Pārbauda, vai numurs sākas ar +371 un ir 8 cipari pēc tam."""
    return text.startswith("+371") and len(text) == 12 and text[4:].isdigit()

def is_valid_age(age):
    """Pārbauda, vai vecums ir robežās no 0 līdz 150."""
    return 0 <= age <= 150

def is_strong_password(text):
    """Vismaz 8 simboli, satur burtus UN ciparus."""
    if len(text) < 8:
        return False
    has_letter = any(c.isalpha() for c in text)
    has_digit = any(c.isdigit() for c in text)
    return has_letter and has_digit

# Šī daļa ir obligāta pēc prasībām (tests)
if __name__ == "__main__":
    print("Testējam e-pastus:")
    print(f"anna@inbox.lv: {is_email('anna@inbox.lv')}") # True
    print(f"anna: {is_email('anna')}") # False
    
    print("\nTestējam telefonus:")
    print(f"+37126123456: {is_phone_number('+37126123456')}") # True
    print(f"26123456: {is_phone_number('26123456')}") # False