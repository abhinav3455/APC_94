def average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(int, input("Enter numbers: ").split()))
print(average(numbers))