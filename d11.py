students = {
    "Rahul": 75,
    "Amit": 92,
    "Sneha": 85,
    "Priya": 88
}

name = max(students, key=students.get)

print("Highest marks:", name)
print("Marks:", students[name])