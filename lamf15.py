students = [
    ("Rahul", 85),
    ("Priya", 92),
    ("Amit", 70),
    ("Sneha", 78)
]

result = sorted(students, key=lambda x: x[1])

print(result)