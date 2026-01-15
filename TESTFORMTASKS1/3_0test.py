class BankAccount:
    def __init__(self, number):
        self.number = number
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient funds on the account"

    def info(self):
        return f"Bank Account No: {self.number}\nBalance: PLN {self.balance:.2f}"

if __name__ == "__main__":
    account = BankAccount("12 3456 5555 9090 1111 0000 7722")
    account.deposit(25.30)
    print(account.info())
    print(account.withdraw(31.70))
    print(account.info())
    print(account.withdraw(14.0))
    print(account.info())