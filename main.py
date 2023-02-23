class BankAccount():
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self):
        add_money = float(input('How much money do you want to add: '))
        print('New blalnce is ', self.balance + add_money)

    def withdraw(self):
        take_money = float(input('How much money would you likt to take: '))
        new_balance = self.balance - take_money
        print('You took', take_money, ". Current balance is ", new_balance)

    def display_balance(self):
        print('Current balance: ', self.balance)

account_1 = BankAccount('Taja', 'Vasilevich', 1000, 'debt', 1234, 378237.23)

account_1.deposit()
account_1.withdraw()
account_1.display_balance()

print(vars(account_1))
