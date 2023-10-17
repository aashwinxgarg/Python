class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposit: +₹{amount}')
            return f'You have successfully deposited ₹{amount}.'
        else:
            return 'Invalid amount for deposit.'

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdraw: -₹{amount}')
            return f'You have successfully withdrawn ₹{amount}.'
        else:
            return 'Invalid amount for withdrawal.'

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f'Transfer to {recipient.user_id}: -₹{amount}')
            recipient.transaction_history.append(f'Transfer from {self.user_id}: +₹{amount}')
            return f'You have successfully transferred ₹{amount} to {recipient.user_id}.'
        else:
            return 'Invalid amount for transfer.'

    def check_balance(self):
        return f'Your account balance is ₹{self.balance}.'

    def get_transaction_history(self):
        return self.transaction_history

class ATM:
    def __init__(self):
        self.users = {}  # Dictionary to store user data

    def create_user(self, user_id, pin):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, pin)
            return f'User {user_id} created successfully.'
        else:
            return f'User {user_id} already exists. Please choose a different User ID.'

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None

# Main program
atm = ATM()

while True:
    print("\nWelcome to the Python ATM")
    print("1. Create User")
    print("2. Login")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_id = input("Enter your User ID: ")
        pin = input("Enter your PIN: ")
        message = atm.create_user(user_id, pin)
        print(message)

    elif choice == "2":
        user_id = input("Enter your User ID: ")
        pin = input("Enter your PIN: ")
        user = atm.authenticate_user(user_id, pin)
        if user:
            print(f"Welcome, {user.user_id}!")
            while True:
                print("\nATM Menu")
                print("1. View Transaction History")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transfer")
                print("5. Check Balance")
                print("6. Logout")

                choice = input("Enter your choice: ")

                if choice == "1":
                    history = user.get_transaction_history()
                    for transaction in history:
                        print(transaction)

                elif choice == "2":
                    amount = float(input("Enter the withdrawal amount: "))
                    message = user.withdraw(amount)
                    print(message)

                elif choice == "3":
                    amount = float(input("Enter the deposit amount: "))
                    message = user.deposit(amount)
                    print(message)

                elif choice == "4":
                    recipient_id = input("Enter the recipient's User ID: ")
                    if recipient_id in atm.users:
                        recipient = atm.users[recipient_id]
                        amount = float(input("Enter the transfer amount: "))
                        message = user.transfer(recipient, amount)
                        print(message)
                    else:
                        print("Recipient not found.")

                elif choice == "5":
                    balance = user.check_balance()
                    print(balance)

                elif choice == "6":
                    print(f"Goodbye, {user.user_id}!")
                    break

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid User ID or PIN. Please try again.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
