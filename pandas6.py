import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Department": ["CSE", "CSE", "IT", "CSE", "IT"],
    "Total_Classes": [100, 100, 120, 100, 80],
    "Classes_Attended": [90, 70, 80, 60, 75]
}

df = pd.DataFrame(data)

# Calculate Attendance Percentage
df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("Student Attendance:")
print(df)

print("\nStudents with Attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])