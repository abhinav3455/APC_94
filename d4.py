marks = {
    "Rahul": 75,
    "Amit": 82,
    "Sneha": 90,
    "Priya": 88
}

name = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))

if name in marks:
    marks[name] = new_marks
    print(marks)
else:
    print("Student not found")