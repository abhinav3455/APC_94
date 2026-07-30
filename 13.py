
n = int(input("Enter a number: "))
temp = abs(n)
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = (reversed_num * 10) + digit
    temp //= 10
if n < 0:
    reversed_num = -reversed_num
print("Reversed number:", reversed_num)