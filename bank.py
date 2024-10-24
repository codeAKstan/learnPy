from main import BankAccount


# Simple bank
def main_menu():
    print("1 for deposit")
    print("2 for withdraw")
    print("3 for balance check")
    print("4 to exit")


def handle_deposit(bank):
    try:
        dep_amt = float(input("Enter the amount you want to deposit: "))
        print(bank.deposit(dep_amt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def handle_withdraw(bank):
    try:
        with_amt = float(input("Enter the amount you want to withdraw: "))
        print(bank.withdraw(with_amt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def main():
    bank = BankAccount()

    while True:
        main_menu()
        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Your choice should be between 1 to 4.")
            except ValueError:
                print("Please enter a valid number.")

        if choice == 1:
            handle_deposit(bank)
        elif choice == 2:
            handle_withdraw(bank)
        elif choice == 3:
            print(bank.check_balance())
        elif choice == 4:
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
