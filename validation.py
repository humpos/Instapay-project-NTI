"""Input validation functions for the InstaPay simulation."""


def validate_username(username):
    username = username.strip()
    return len(username) >= 3 and username.replace("_", "").isalnum()


def validate_password(password):
    return len(password) >= 6


def validate_phone(phone):
    # Egyptian-style mobile number: 11 digits and starts with 01.
    return phone.isdigit() and len(phone) == 11 and phone.startswith("01")


def validate_amount(value):
    try:
        amount = float(value)
        return amount > 0
    except ValueError:
        return False


def validate_card_number(card_number):
    cleaned = card_number.replace(" ", "")
    return cleaned.isdigit() and len(cleaned) == 16


def validate_cvv(cvv):
    return cvv.isdigit() and len(cvv) in (3, 4)


def validate_expiry_date(expiry):
    # Basic MM/YY validation.
    if len(expiry) != 5 or expiry[2] != "/":
        return False

    month, year = expiry.split("/")
    if not (month.isdigit() and year.isdigit()):
        return False

    return 1 <= int(month) <= 12


def format_amount(amount):
    amount = float(amount)
    if amount.is_integer():
        return str(int(amount))
    return f"{amount:.2f}"
