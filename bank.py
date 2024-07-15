class bank_account:
    def __init__(self):
        self.amount = 0

    def deposit(self, Amount):
        self.amount += Amount
        print(f"Amount Succesfully Deposited.\nCurrent amount is {self.amount}")

    def withdraw(self, Amount):
        if (self.amount - Amount >= 0):
            self.amount -= Amount
            print(f"Amount Succesfully Withdraw.\nCurrent amount is {self.amount}")

        else:
            print("Insufficient balance!!")

    def display(self):
        print(f"Your balance is {self.amount}")


ba = bank_account()
while True:

    print("1.Deposit 2.Withdraw 3.Display 4.Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        Amount = float(input("Enter the amount of Deposit: "))
        ba.deposit(Amount)
    elif option == 2:
        Amount = float(input("Enter the amount of Withdraw: "))
        ba.withdraw(Amount)
    elif option == 3:
        ba.display()
    elif option == 4:
        print("Succesfully Exited")
        break
    else:
        print("Error please try again!")




