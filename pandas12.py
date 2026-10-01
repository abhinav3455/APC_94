import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# 1. Display first 5 records
print("First 5 Records:")
print(df.head())

# 2. Display last 5 records
print("\nLast 5 Records:")
print(df.tail())

# 3. Calculate Total and Average marks
df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average Marks:")
print(df)

# 4. Students whose average is greater than 75
print("\nStudents with Average greater than 75:")
print(df[df["Average"] > 75])

# 5. Student with highest average
print("\nStudent with Highest Average:")
print(df.loc[df["Average"].idxmax()])

# 6. Average marks for each subject
print("\nAverage Marks of Each Subject:")

print("Python:", df["Python"].mean())
print("DBMS:", df["DBMS"].mean())
print("Maths:", df["Maths"].mean())