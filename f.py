import math

x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms (even): "))
total = 0.0
sign = 1
fact = 1
x_power = 1
for i in range(0, n + 1, 2):
    if i == 0:
        x_power = 1
        fact = 1
    else:
        x_power *= x * x
        fact *= i * (i - 1)
    total += sign * (x_power / fact)
    sign *= -1

print("cos(x) ≈", total)
print("math.cos(x) =", math.cos(x))