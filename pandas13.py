import pandas as pd

# Read CSV file
df = pd.read_csv("employees.csv")

# 1. Display employees from CSE department
print("Employees from CSE Department:")
print(df[df["Department"] == "CSE"])

# 2. Find average salary
print("\nAverage Salary:")
print(df["Salary"].mean())

# 3. Find highest and lowest salary
print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

# 4. Display employees having salary greater than 50000
print("\nEmployees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])

# 5. Department-wise average salary
print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())