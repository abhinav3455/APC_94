def number_summary(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
        total += num

    avg = total / len(numbers)

    return minimum, maximum, total, avg

numbers = list(map(int, input("Enter numbers: ").split()))

minimum, maximum, total, avg = number_summary(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", avg)