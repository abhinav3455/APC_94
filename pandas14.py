import pandas as pd

# Read CSV file
df = pd.read_csv("patients.csv")

# 1. Display patients above 60 years
print("Patients above 60 years:")
print(df[df["Age"] > 60])

# 2. Calculate average medical expense
print("\nAverage Medical Expense:")
print(df["Medical_Expense"].mean())

# 3. Find patient with highest medical expense
print("\nPatient with Highest Medical Expense:")
print(df.loc[df["Medical_Expense"].idxmax()])

# 4. Count patients for each disease
print("\nNumber of Patients for Each Disease:")
print(df["Disease"].value_counts())

# 5. Display patients whose medical expense exceeds 50000
print("\nPatients with Medical Expense greater than 50000:")
print(df[df["Medical_Expense"] > 50000])