def largest_element(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = list(map(int, input("Enter numbers: ").split()))
print(largest_element(numbers))