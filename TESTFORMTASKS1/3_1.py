class BankAccount:
    def __init__(self, number):
        self.number = number
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return ""
        else:
            return "Insufficient funds on the account"

    def info(self):
        #formatted_balance = f"{self.balance:.2f}".replace('.', ',')
        #return f"Bank Account No: {self.number}\nBalance: PLN {formatted_balance}"
        return f"Bank Account No: {self.number}\nBalance: PLN {f"{self.balance:.2f}".replace('.', ',')}"
if __name__ == "__main__":
    account = BankAccount("12 3456 5555 9090 1111 0000 7722")
    
    print(account.info())
    
    account.deposit(25.30)
    
    print(account.info())
    
    if not account.withdraw(31.70):
        print("Insufficient funds on the account")
    
    print(account.info())
    
    if not account.withdraw(14.0):
        print("Insufficient funds on the account")
        
    print(account.info())