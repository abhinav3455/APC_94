numbers = [1, 2, 3, 2, 4, 1, 3, 3, 5]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)