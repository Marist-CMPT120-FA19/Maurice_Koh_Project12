class Customer:

    def __init__(self, id, pin, checking_balance, savings_balance):
        self.id = id
        self.pin = pin
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance

    def get_id(self):
        return self.id

    def get_pin(self):
        return self.pin

    def get_checking_bal(self):
        return self.checking_balance

    def get_savings_bal(self):
        return self.savings_balance

    def withdraw(self, amount, account):
        if account == 'c':
            self.checking_balance -= amount
        elif account == 's':
            self.savings_balance -= amount
        else:
            print("Please enter a valid account type")

    def deposit(self, amount, account):
        if account == 'c':
            self.checking_balance += amount
        elif account == 's':
            self.savings_balance += amount
        else:
            print("Please enter a valid account type")

    def transfer(self, amount, account1, account2):
        if account1 == 'c' and account2 == 's':
            account1 -= amount
            account2 += amount
        elif account1 == 's' and account2 == 'c':
            account1 -= amount
            account2 += amount
        else:
            print("Invalid input: please try again")

            
        
