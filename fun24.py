balance = 0
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposit: " + str(amount))

def withdrawal(amount):
    global balance

    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawal: " + str(amount))
        return True
    else:
        return False

def balance_enquiry():
    return balance

def transaction_history():
    return transactions

deposit(5000)
withdrawal(1500)
withdrawal(5000)

print("Balance:", balance_enquiry())
print("Transactions:", transaction_history())