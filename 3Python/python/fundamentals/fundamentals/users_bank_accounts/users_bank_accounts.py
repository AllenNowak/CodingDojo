class User:
    default_account_type = 'Savings'

    def __init__(self, name, email, typ=default_account_type):
        self.name = name
        self.email = email
        self.account = Bank_Account(interest_rate=0.02, starting_balance=0)
        self.accounts = []
        self.accounts.append({'Type': typ, 'Account': self.account})

    def __str__(self):
        insides = f'''
        Account Owner: {self.name}
        Accounts: {len(self.accounts)}'''
        extra = ''
        for record in self.accounts:
            extra += f'\n\t{record["Type"]} : {record["Account"]}'

        insides += extra
        return insides

    def get_account_for_type(self, key):
        the_list = [acc for acc in self.accounts if acc['Type'] == key]
        if (len(the_list) == 1):
            return the_list[0]['Account']
        return None

    def add_account(self, interest_rate, account_type=default_account_type):
        types = [key['Type']for key in self.accounts if key['Type'] == account_type]
        if account_type in types:
            print(
                f'account type {account_type} already exists in accounts, no account added')
        else:
            self.accounts.append(
                {'Type': account_type, 'Account': Bank_Account(interest_rate)})
        return self

    def make_deposit(self, amount, account_type=default_account_type):
        the_account = self.get_account_for_type(account_type)
        if the_account is not None:
            the_account.deposit(amount)
            # print(f'Depositing {amount} into {account_type}, new balance = {the_account.balance}')
        else:
            print(f'Cannot complete deposit to {account_type} account')

        return self

    def make_withdrawl(self, amount, account_type=default_account_type):
        the_account = self.get_account_for_type(account_type)
        if the_account is not None:
            the_account.withdraw(amount)
            # print(f'Withdrawing {amount} from {account_type}, new balance = {the_account.balance}')
        else:
            print(f'Cannot complete withdrawl from {account_type} account')

 
        return self

    def transfer_money(self, amount, other_user, account_type=default_account_type):
        the_account = self.get_account_for_type(account_type)
        if the_account is None:
            print(f'Cannot complete transfer. Problem with {account_type} account')
            return self

        if (amount > the_account.balance):
            print('Insufficient funds')
        else:
            the_account.withdraw(amount)
            other_user.make_deposit(amount)
            # print(f'Withdrawing {amount} from {account_type}, new balance = {the_account.balance}')
            # print(f'Depositing {amount} into {other_user}'s {account_type}, new balance = {the_account.balance}')
        return self


class Bank_Account:
    all_accounts = []

    def __init__(self, interest_rate, starting_balance=0):
        self.balance = starting_balance
        self.interest_rate = interest_rate
        Bank_Account.all_accounts.append(self)

    def __str__(self):
        return f'Balance: {self.balance}, Interest Rate: {self.interest_rate}'

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (amount < self.balance):
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
        for x in cls.all_accounts:
            print(f'Balance: {x.balance}, Interest Rate: {x.interest_rate}')


account1 = Bank_Account(0.1)
account2 = Bank_Account(0.15)

print('Account 1 Chaining deposits')
account1.deposit(5).deposit(10).deposit(95).withdraw(10).yield_interest().display_account_info()
print('Account 2 Chaining deposits into account2')
account2.deposit(75).deposit(100).withdraw(5).withdraw(25).withdraw(25).withdraw(20).yield_interest().display_account_info()

print('Displaying all account info on the BankAccount')
Bank_Account.all_info()

print(f"\nUser 3's Bank Accounts3")
user3 = User('Steve', 'foo@email')
print('\nAdding more account types')
user3.add_account(0.0, 'Checking')
user3.add_account(0.1, 'Mutual Fund')
user3.add_account(0.5, 'Mutual Fund')
print(f'# of accounts: {len(user3.accounts)}')

print('\nWorking on User 4')
user4 = User('Alan', 'bar@baz.com', 'CD')
user4.add_account(0.25, 'Mutual Fund')
user4.add_account(0.5, 'Savings')
user4.add_account(1.5, 'Checking')

user4.make_deposit(10, 'Mutual Fund').make_deposit(10, 'Mutual Fund').make_deposit(10, 'Mutual Fund')
user4.make_deposit(5, 'Savings').make_deposit(5, 'Savings').make_deposit(5, 'Savings')
user4.make_deposit(33, 'Checking').make_deposit(33, 'Checking').make_deposit(33, 'Checking')
print('Before Withdrawing money from Savings')
print(f'\nuser 4 = {user4}')
user4.make_withdrawl(12, 'Savings')
print('After withdrawing 12 from Savings')
print(f'\nuser 4 = {user4}')

print()
print("Before transfering money from user 4's Checking to user 3")
print(f'User 4: {user4}')
print(f'User 3: {user3}')
user4.transfer_money(90, user3, 'Checking')
print("After transfering 90 from user 4's Checking to user 3's Savings")
print(f'User 4: {user4}')
print(f'User 3: {user3}')


