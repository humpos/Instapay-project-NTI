"""Registration and authentication logic."""

from validation import validate_username, validate_password, validate_phone


# In-memory storage for this console application.
users = {}


def find_user(username):
    return users.get(username)


def register():
    print("\n===== Register =====")

    while True:
        name = input("Full name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    while True:
        phone = input("Phone number: ").strip()
        if validate_phone(phone):
            break
        print("Invalid phone number. Enter 11 digits starting with 01.")

    while True:
        username = input("Username: ").strip()

        if not validate_username(username):
            print("Username must be at least 3 characters and contain only letters, numbers, or underscores.")
        elif find_user(username):
            print("This username already exists. Choose another one.")
        else:
            break

    while True:
        password = input("Password: ")
        if validate_password(password):
            break
        print("Password must contain at least 6 characters.")

    users[username] = {
        "name": name,
        "phone": phone,
        "password": password,
        "balance": 10000.0,
        "card": None,
        "transactions": []
    }

    print(f"\nRegistration successful! You can now log in as {username}.")
    return username


def login(max_attempts=3):
    print("\n===== Login =====")

    for attempt in range(1, max_attempts + 1):
        username = input("Username: ").strip()
        password = input("Password: ")

        user = find_user(username)

        if user and user["password"] == password:
            print(f"\nLogin successful! Welcome {user['name']}.")
            return username

        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Invalid username or password. Attempts remaining: {remaining}")
        else:
            print("Login failed. Maximum attempts reached.")

    return None
