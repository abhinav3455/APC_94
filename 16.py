
n = int(input("Enter total count of numbers (n): "))
if n > 0:
    count = 1
    smallest = float(input("Enter number 1: "))
    while count < n:
        count += 1
        num = float(input(f"Enter number {count}: "))
        if num < smallest:
            smallest = num
    print("Smallest number:", smallest)
else:
    print("Invalid count.")