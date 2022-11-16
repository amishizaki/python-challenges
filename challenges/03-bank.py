current_balance = 40000

def bank_visit():
    prompt = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    if (prompt == 'deposit'):
        deposit()
    elif (prompt == 'withdraw'):
        withdraw()
    elif (prompt == 'check_balance'):
        check_balance()

    double_check = input("Anything else you'd like to do? (y/n) ")
    if (double_check.lower() == 'y'):
        bank_visit()
        return
    else:
        print("Thank you!")
        return

def check_balance():
    global current_balance
    print(f"Your current balance is {current_balance}")

def deposit():
    amount = input('How much would you like to deposit? \n')
    global current_balance
    current_balance += int(amount)
    print(f"Your new balance is {current_balance}")

def withdraw():
    amount = input('How much would you like to withdraw? \n')
    global current_balance
    current_balance -= int(amount)
    print(f"Your new balance is {current_balance}")

print("Welcome to the Bank.")
bank_visit()
print("Come again!")

