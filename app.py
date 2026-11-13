# =====================================
# SIMPLE SMART BANKING MANAGEMENT SYSTEM
# =====================================

accounts = {}
transactions = []

next_account_number = 1001


# CREATE ACCOUNT
def create_account():

    global next_account_number

    print("\n----- CREATE ACCOUNT -----")

    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")

    if not phone.isdigit() or len(phone) != 10:
        print("Enter a valid 10-digit phone number!")
        return

    # CHECK DUPLICATE PHONE
    for account in accounts.values():

        if account["phone"] == phone:
            print("Phone number already registered!")
            return

    pin = input("Create 4-digit PIN: ")

    if not pin.isdigit() or len(pin) != 4:
        print("PIN must contain exactly 4 digits!")
        return

    accounts[next_account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0
    }

    print("\nAccount created successfully!")
    print("Account Number:", next_account_number)

    next_account_number += 1


# CUSTOMER LOGIN
def customer_login():

    print("\n----- CUSTOMER LOGIN -----")

    try:
        account_number = int(input("Enter account number: "))

    except ValueError:
        print("Invalid account number!")
        return

    if account_number not in accounts:
        print("Account not found!")
        return

    pin = input("Enter 4-digit PIN: ")

    if pin == accounts[account_number]["pin"]:

        print("\nLogin successful!")
        print("Welcome,", accounts[account_number]["name"])

        customer_menu(account_number)

    else:
        print("Incorrect PIN!")


# CUSTOMER MENU
def customer_menu(account_number):

    while True:

        print("\n========== CUSTOMER MENU ==========")

        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Account Details")
        print("5. Transaction History")
        print("6. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit_money(account_number)

        elif choice == "3":
            withdraw_money(account_number)

        elif choice == "4":
            account_details(account_number)

        elif choice == "5":
            transaction_history(account_number)

        elif choice == "6":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice! Try again.")


# CHECK BALANCE
def check_balance(account_number):

    balance = accounts[account_number]["balance"]

    print("\nAvailable Balance: ₹", balance)


# DEPOSIT MONEY
def deposit_money(account_number):

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Enter an amount greater than zero!")
            return

        accounts[account_number]["balance"] += amount

        transactions.append({
            "account": account_number,
            "type": "Deposit",
            "amount": amount
        })

        print("Money deposited successfully!")

        print(
            "New Balance: ₹",
            accounts[account_number]["balance"]
        )

    except ValueError:
        print("Please enter a valid amount!")


# WITHDRAW MONEY
def withdraw_money(account_number):

    try:
        amount = float(input("Enter withdrawal amount: "))

        balance = accounts[account_number]["balance"]

        if amount <= 0:
            print("Enter an amount greater than zero!")

        elif amount > balance:
            print("Insufficient balance!")

        else:

            accounts[account_number]["balance"] -= amount

            transactions.append({
                "account": account_number,
                "type": "Withdrawal",
                "amount": amount
            })

            print("Money withdrawn successfully!")

            print(
                "Remaining Balance: ₹",
                accounts[account_number]["balance"]
            )

    except ValueError:
        print("Please enter a valid amount!")


# ACCOUNT DETAILS
def account_details(account_number):

    print("\n----- ACCOUNT DETAILS -----")

    print("Account Number:", account_number)

    print("Customer Name:",
          accounts[account_number]["name"])

    print("Phone Number:",
          accounts[account_number]["phone"])

    print("Balance: ₹",
          accounts[account_number]["balance"])


# TRANSACTION HISTORY
def transaction_history(account_number):

    print("\n----- TRANSACTION HISTORY -----")

    found = False

    for transaction in transactions:

        if transaction["account"] == account_number:

            print("Transaction Type:", transaction["type"])

            print("Amount: ₹", transaction["amount"])

            found = True

    if not found:
        print("No transactions available!")


# FORGOT PIN
def forgot_pin():

    print("\n----- FORGOT PIN -----")

    try:
        account_number = int(input("Enter account number: "))

    except ValueError:
        print("Invalid account number!")
        return

    if account_number not in accounts:

        print("Account not found!")
        return

    phone = input("Enter registered phone number: ")

    if phone == accounts[account_number]["phone"]:

        new_pin = input("Enter new 4-digit PIN: ")

        if new_pin.isdigit() and len(new_pin) == 4:

            accounts[account_number]["pin"] = new_pin

            print("\nPIN changed successfully!")

        else:
            print("PIN must contain exactly 4 digits!")

    else:
        print("Incorrect phone number!")


# =====================================
# MAIN MENU
# =====================================

while True:

    print("\n================================")
    print("       SMART BANKING SYSTEM")
    print("================================")

    print("1. Create Account")
    print("2. Customer Login")
    print("3. Forgot PIN")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        create_account()

    elif choice == "2":

        customer_login()

    elif choice == "3":

        forgot_pin()

    elif choice == "4":

        print("\nThank you for using Smart Banking System!")
        print("Have a nice day!")

        break

    else:

        print("Invalid choice! Please try again.")