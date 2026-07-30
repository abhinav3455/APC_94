
n = int(input("Enter a number: "))
num = n
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(f"Factorial of {n}:", factorial)