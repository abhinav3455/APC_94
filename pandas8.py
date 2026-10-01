import pandas as pd

marks = {
    "Amit": 80,
    "Rahul": 65,
    "Sneha": 90,
    "Priya": 72,
    "Rohit": 85
}

s = pd.Series(marks)

print("Student Marks:")
print(s)

print("\nMarks of Sneha:")
print(s["Sneha"])

print("\nMaximum Marks:")
print(s.max())

print("\nMinimum Marks:")
print(s.min())

print("\nAverage Marks:")
print(s.mean())

print("\nStudents who scored more than 75:")
print(s[s > 75])