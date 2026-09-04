# InstaPay Simulation

A console-based digital wallet simulation built using core Python concepts.

## Project Structure

```text
instapay_simulation/
├── main.py          # Menus and application flow
├── auth.py          # Registration and login
├── validation.py    # Input validation
├── operations.py    # Wallet and money operations
└── README.md
```

## Features

- Register with full name, phone number, username, and password
- Unique username validation
- Password validation (minimum 6 characters)
- Egyptian phone number validation
- Login with a maximum of 3 attempts
- Link a Visa card with basic validation
- View balance
- Deposit money
- Withdraw money without exceeding the balance
- Transfer money to another registered user
- Transfer confirmation
- Transaction history using a list of dictionaries
- Graceful handling of invalid input
- Multi-file organization using Python modules

## Important Note

This is an educational simulation. User data is stored only while the program is running and is not saved to a database or file.

## How to Run

Open a terminal inside the project folder and run:

```bash
python main.py
```

## Suggested Demo Scenario

1. Register user A.
2. Register user B.
3. Log in as user A.
4. Link a Visa card.
5. Deposit money.
6. View the balance.
7. Transfer money to user B.
8. Withdraw money.
9. View transaction history.
10. Log out.

Then the application returns to the main menu and continues running until the user chooses **Exit**.
