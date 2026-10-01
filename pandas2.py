import pandas as pd

data = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Employee_Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Department": ["CSE", "IT", "HR", "CSE", "IT"],
    "Salary": [45000, 60000, 55000, 75000, 50000],
    "Experience": [2, 5, 4, 8, 6]
}

df = pd.DataFrame(data)

print("Employee Data:")
print(df)

print("\nEmployees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nEmployee with Highest Experience:")
print(df.loc[df["Experience"].idxmax()])