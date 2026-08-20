students = {
    "Rahul": "Computer",
    "Amit": "IT",
    "Sneha": "Computer",
    "Priya": "ENTC",
    "Rohan": "IT"
}

departments = {}

for name, department in students.items():
    if department not in departments:
        departments[department] = []
    departments[department].append(name)

print(departments)