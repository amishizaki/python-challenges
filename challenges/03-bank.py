class BankAccount():
    def __init__(self):
        self.balance = 40000
        print("Welcome to Chase bank.")
        
    
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
print (my_acct)
prompt = input('What would you like to do? (deposit, withdraw, check_balance)\n')
if (prompt == 'deposit'):
    my_acct.deposit
elif (prompt == 'withdraw'):
    my_acct.withdraw
elif (prompt == 'check_balance'):
    print(my_acct.balance)
# double_check = input("Anything else you'd like to do? (y/n) ")




    # if (double_check == 'y'):
        

print("Have a nice day!")

