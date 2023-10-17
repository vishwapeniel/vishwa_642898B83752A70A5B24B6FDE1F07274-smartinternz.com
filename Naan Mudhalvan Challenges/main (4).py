class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance")

    def display(self):
        print("\nNet Available Balance =", self.balance)

# Driver code

# creating an object of the class
s = Bank_Account()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
