
n = int(input("Enter total count of numbers (n): "))
if n > 0:
    count = 1
    largest = float(input("Enter number 1: ")) 
    while count < n:
        count += 1
        num = float(input(f"Enter number {count}: "))
        if num > largest:
            largest = num  
    print("Largest number:", largest)
else:
    print("Invalid count.")