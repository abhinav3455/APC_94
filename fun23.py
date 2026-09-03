def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / 5

def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"

def process_students(students):
    results = []

    for student in students:
        total = total_marks(student["marks"])
        per = percentage(student["marks"])
        grd = grade(per)

        results.append({
            "name": student["name"],
            "roll": student["roll"],
            "total": total,
            "percentage": per,
            "grade": grd
        })

    class_average = sum(s["percentage"] for s in results) / len(results)
    highest = max(results, key=lambda s: s["percentage"])
    lowest = min(results, key=lambda s: s["percentage"])

    return results, class_average, highest, lowest

students = [
    {"name": "Amit", "roll": 1, "marks": [80, 75, 90, 85, 88]},
    {"name": "Rahul", "roll": 2, "marks": [70, 65, 75, 72, 68]},
    {"name": "Priya", "roll": 3, "marks": [95, 92, 90, 96, 94]}
]

results, class_average, highest, lowest = process_students(students)

for student in results:
    print(student)

print("Class Average:", class_average)
print("Highest Scorer:", highest["name"])
print("Lowest Scorer:", lowest["name"])