"""Wallet, card, and transaction operations."""

from validation import (
    validate_amount,
    validate_card_number,
    validate_cvv,
    validate_expiry_date,
    format_amount,
)
from auth import find_user


def add_transaction(user, transaction):
    # Transaction history is stored as a list of dictionaries.
    user["transactions"].append(transaction)


def show_balance(username):
    user = find_user(username)
    if user:
        print(f"\nCurrent Balance: {format_amount(user['balance'])} EGP")


def link_card(username):
    user = find_user(username)
    if not user:
        return

    print("\n===== Link Visa Card =====")

    while True:
        card_number = input("Card number (16 digits): ").strip().replace(" ", "")
        if validate_card_number(card_number):
            break
        print("Invalid card number.")

    while True:
        holder_name = input("Card holder name: ").strip()
        if holder_name:
            break
        print("Card holder name cannot be empty.")

    while True:
        expiry_date = input("Expiry date (MM/YY): ").strip()
        if validate_expiry_date(expiry_date):
            break
        print("Invalid expiry date.")

    while True:
        cvv = input("CVV: ").strip()
        if validate_cvv(cvv):
            break
        print("Invalid CVV.")

    # CVV is intentionally not displayed after this operation.
    user["card"] = {
        "number": card_number,
        "holder_name": holder_name,
        "expiry_date": expiry_date,
        "cvv": cvv
    }

    print("Card linked successfully!")


def deposit(username):
    user = find_user(username)
    if not user:
        return

    print("\n===== Deposit =====")
    while True:
        amount_text = input("Enter amount: ").strip()
        if validate_amount(amount_text):
            amount = float(amount_text)
            break
        print("Invalid amount. Amount must be greater than 0.")

    user["balance"] += amount
    add_transaction(user, {
        "type": "Deposit",
        "amount": amount
    })

    print("Deposit successful!")
    print(f"New Balance: {format_amount(user['balance'])} EGP")


def withdraw(username):
    user = find_user(username)
    if not user:
        return

    print("\n===== Withdraw =====")
    while True:
        amount_text = input("Enter amount: ").strip()

        if not validate_amount(amount_text):
            print("Invalid amount. Amount must be greater than 0.")
            continue

        amount = float(amount_text)

        if amount > user["balance"]:
            print("Insufficient balance.")
            continue

        break

    user["balance"] -= amount
    add_transaction(user, {
        "type": "Withdraw",
        "amount": amount
    })

    print("Withdrawal successful!")
    print(f"Remaining Balance: {format_amount(user['balance'])} EGP")


def transfer(username):
    sender = find_user(username)
    if not sender:
        return

    print("\n===== Transfer =====")
    recipient_username = input("Recipient username: ").strip()

    if recipient_username == username:
        print("You cannot transfer money to yourself.")
        return

    recipient = find_user(recipient_username)
    if not recipient:
        print("Recipient does not exist.")
        return

    amount_text = input("Amount: ").strip()
    if not validate_amount(amount_text):
        print("Invalid amount. Amount must be greater than 0.")
        return

    amount = float(amount_text)

    if amount > sender["balance"]:
        print("Insufficient balance.")
        return

    confirmation = input(
        f"Confirm transfer of {format_amount(amount)} EGP to {recipient_username}? (yes/no): "
    ).strip().lower()

    if confirmation != "yes":
        print("Transfer cancelled.")
        return

    sender["balance"] -= amount
    recipient["balance"] += amount

    add_transaction(sender, {
        "type": "Transfer",
        "amount": amount,
        "to": recipient_username
    })

    add_transaction(recipient, {
        "type": "Received Transfer",
        "amount": amount,
        "from": username
    })

    print("Transfer successful!")
    print(f"Your new balance: {format_amount(sender['balance'])} EGP")


def show_transactions(username):
    user = find_user(username)
    if not user:
        return

    print("\n===== Transaction History =====")

    transactions = user["transactions"]

    if not transactions:
        print("No transactions found.")
        return

    for index, transaction in enumerate(transactions, start=1):
        transaction_type = transaction["type"]
        amount = transaction["amount"]

        if transaction_type in ("Deposit", "Received Transfer"):
            sign = "+"
        else:
            sign = "-"

        details = ""
        if "to" in transaction:
            details = f" -> {transaction['to']}"
        elif "from" in transaction:
            details = f" <- {transaction['from']}"

        print(
            f"{index}. {transaction_type}{details}    "
            f"{sign}{format_amount(amount)} EGP"
        )
