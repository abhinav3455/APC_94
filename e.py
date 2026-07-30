n = int(input("Enter n: "))
total = 1.0
fact = 1
for i in range(1, n + 1):
    fact *= i
    total += 1.0 / fact

print("Sum =", total)