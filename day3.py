class BankAccount:
    def __init__(self,acc_no,acc_holder,balance):
        self.balance=balance
        self.acc_no=acc_no
        self.acc_holder=acc_holder
        self.history = []
    
    def deposit(self,amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.balance+=amount
        self.history.append(f"Deposited: {amount}")
        print(f"Deposited: {amount}")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            self.history.append(f"Deposited: {amount}")
            print(f"Withdrawn: {amount}")
            
    def display_account(self):
        print("\n ACCOUNT DETAILS ")
        print(f"Account Number : {self.acc_no}")
        print(f"Account Holder : {self.acc_holder}")
        print(f"Balance        : {self.balance}")

    def show_history(self):
        print("\n TRANSACTION HISTORY ")
        if not self.history:
            print("No transactions found.")
        else:
            for transaction in self.history:
                print(transaction)

class SavingsAccount (BankAccount):
    def __init__(self, acc_no, acc_holder, balance,interest_rate):
        super().__init__(acc_no, acc_holder, balance)
        self.interest_rate=interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        self.history.append(f"Interest Added: {interest}")
        print(f"Interest Added: {interest}")

class CurrentAccount(BankAccount):
    def __init__(self, acc_no, acc_holder, balance ,overdraft_limit):
        super().__init__(acc_no, acc_holder, balance)
        self.overdraft_limit=overdraft_limit

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return
        available_balance = self.balance + self.overdraft_limit
        if amount > available_balance:
            print(
                f"Insufficient balance. "
                f"Available amount: {available_balance}"
            )
        else:
            self.balance -= amount
            self.history.append(f"Withdrawn: {amount}")
            print(f"Withdrawn: {amount}")

print(" BANK ACCOUNT SYSTEM ")

print("\n1. Savings Account")
print("2. Current Account")

account_type = int(input("Choose account type: "))

acc_no = input("Enter Account Number: ")
acc_holder = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))

if account_type == 1:
    interest_rate = float(input("Enter Interest Rate (%): "))

    account = SavingsAccount(
        acc_no,
        acc_holder,
        balance,
        interest_rate
    )

elif account_type == 2:
    overdraft_limit = float(input("Enter Overdraft Limit: "))

    account = CurrentAccount(
        acc_no,
        acc_holder,
        balance,
        overdraft_limit
    )

else:
    print("Invalid account type")
    exit()

while True:
    print("\n BANK MENU ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Account")
    print("4. Transaction History")

    if isinstance(account, SavingsAccount):
        print("5. Add Interest")

    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.display_account()

    elif choice == 4:
        account.show_history()

    elif choice == 5 and isinstance(account, SavingsAccount):
        account.add_interest()

    elif choice == 0:
        print("Thank you!")
        break

    else:
        print("Invalid choice")

