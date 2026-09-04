"""Entry point and menus for the InstaPay Simulation."""

from auth import register, login
from operations import (
    show_balance,
    link_card,
    deposit,
    withdraw,
    transfer,
    show_transactions,
)


def main_menu(username):
    while True:
        print("\n===== Main Menu =====")
        print("1. View Balance")
        print("2. Link Card")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Transaction History")
        print("7. Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            show_balance(username)
        elif choice == "2":
            link_card(username)
        elif choice == "3":
            deposit(username)
        elif choice == "4":
            withdraw(username)
        elif choice == "5":
            transfer(username)
        elif choice == "6":
            show_transactions(username)
        elif choice == "7":
            print("Logged out successfully.")
            return
        else:
            print("Invalid choice. Please choose a number from 1 to 7.")


def run_app():
    while True:
        print("\n===== InstaPay =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                main_menu(username)
        elif choice == "3":
            print("Thank you for using InstaPay Simulation. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    run_app()
