n = int(input("Enter n: "))

for i in range(1, n + 1):
    line = ""
    for _ in range(i):
        line += str(i) + " "
    print(line.strip())