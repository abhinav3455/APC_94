students = {
    "Rahul": 75,
    "Amit": 92,
    "Sneha": 65,
    "Priya": 88
}

name = min(students, key=students.get)

print("Lowest marks:", name)
print("Marks:", students[name])