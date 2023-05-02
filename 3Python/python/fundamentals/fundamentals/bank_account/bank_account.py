class Bank_Account:
    all_accounts = []

    def __init__(self, interest_rate, starting_balance = 0):
        self.balance = starting_balance
        self.interest_rate = interest_rate
        Bank_Account.all_accounts.append(self)
    def __str__(self):
        print(f'Balance: {self.balance}, Interest Rate: {self.interest_rate}')

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(amount < self.balance):
            self.balance -= amount
        else:
            fee = 5
            print(f'Insufficient funds: Charging a ${fee} fee')
            self.balance -= fee
        return self
    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self
    def yield_interest(self):
        self.balance += ((self.balance * self.interest_rate)) if self.balance > 0 else 0
        return self
    @classmethod 
    def all_info(cls):
        # [x for x in cls.all_accounts]
        for x in cls.all_accounts:
            print(f'Balance: {x.balance}, Interest Rate: {x.interest_rate}')
        



account1 = Bank_Account(0.1)
account2 = Bank_Account(0.15)

account1.deposit(5).deposit(10).deposit(95).withdraw(10).yield_interest().display_account_info()
account2.deposit(75).deposit(100).withdraw(5).withdraw(25).withdraw(25).withdraw(20).yield_interest().display_account_info()

print('Trying to display all account info')
Bank_Account.all_info()
