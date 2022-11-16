class BankAccount():
    def __init__(self):
        self.balance = 40000
        print("Welcome to Chase bank.")
        prompt = input('What would you like to do? (deposit, withdraw, check_balance)\n')
        if (prompt == 'deposit'):
            self.deposit
        elif (prompt == 'withdraw'):
            self.withdraw
        elif (prompt == 'check_balance'):
            print(self.balance)
        # double_check = input("Anything else you'd like to do? (y/n) ")
    
    def __str__(self):
        status = (f'balance: {self.balance}')
        return status

    def deposit(self, amount):
        print(self.balance)
        self.balance += input('How much would you like to deposit? ' + int(amount))

    def withdraw(self, amount):
        self.balance -= input('How much would you like to withdraw? ' + int(amount))
        return amount

my_acct = BankAccount()




    # if (double_check == 'y'):
        

print("Have a nice day!")

