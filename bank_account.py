class BalanaceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete")
        self.getBalance()
    
    def viableTx(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanaceException(
                f"\nSorry, account {self.name}' only has a balance of ${self.balance:.2f}"
            )
    def withdraw(self, amount):
        try:
            self.viableTx(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete")
            self.getBalance()
        except BalanaceException as error:
            print(f"\nWithdraw interrupted: {error}")
    def transfer(self, amount, account):
        try:
            print('\n*************\n\nBeginning Transfer.....🚀🚀🚀')
            self.viableTx(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ✅✅\n\n*************')
        except BalanaceException as error:
            print(f'\nTransfe interrupted. ❌❌❌ {error}')

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTx(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Completed")
            self.getBalance()
        except BalanaceException as error:
            print(f"\nWithdrawal interrupted: {error}")
        return super().withdraw(amount)