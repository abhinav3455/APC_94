def second_largest(numbers):
    numbers = list(set(numbers))
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[-2]

numbers = list(map(int, input("Enter numbers: ").split()))
print(second_largest(numbers))