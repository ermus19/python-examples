
class Account:

    account_count = 0
    total_balance = 0

    def __init__(self, name, description, balance):
        self.name = name
        self.balance = balance
        self.description = description
        Account.account_count += 1
        Account.total_balance += self.balance

    def displayCount():
        print("Number of accounts: %d" % Account.account_count)

    def displayTotal():
        print("Total capital: ", Account.total_balance)

    def displayBalance(self):
        print("Balance of account ", self.name, " = ", self.balance)

    def displayAccount(self):
        print("Name: ", self.name, ", Description: ", self.description, " Balance: ", self.balance)


account1 = Account("Test1", "Test account", 34000)
account2 = Account ("Test2", "Test account", 45603.67)

account1.displayBalance()

Account.displayCount()

account3 = Account("Test3", "Test account", 35465)

Account.displayTotal()

print("Total accounts: %d" % Account.account_count)

account1.displayAccount()