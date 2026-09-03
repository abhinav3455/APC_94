f = open("transactions.txt", "w")
f.write("deposit,5000\n")
f.write("withdrawal,1000\n")
f.write("deposit,3000\n")
f.write("withdrawal,500\n")
f.close()

f = open("transactions.txt", "r")

deposits = 0
withdrawals = 0
transactions = []

for line in f:
    typ, amount = line.strip().split(",")
    amount = float(amount)
    transactions.append(amount)

    if typ == "deposit":
        deposits += amount
    else:
        withdrawals += amount

f.close()

balance = deposits - withdrawals
largest = max(transactions)

print("Total deposits:", deposits)
print("Total withdrawals:", withdrawals)
print("Final balance:", balance)
print("Largest transaction:", largest)