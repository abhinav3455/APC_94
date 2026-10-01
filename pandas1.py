import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Python": [80, 70, 90, 65, 85],
    "DBMS": [75, 80, 88, 70, 90],
    "Mathematics": [85, 72, 92, 68, 80]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average:")
print(df)

print("\nStudents with Average greater than 75:")
print(df[df["Average"] > 75])