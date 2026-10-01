import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Age": [65, 45, 70, 30, 62],
    "Disease": ["Diabetes", "Fever", "Heart", "Cold", "Diabetes"],
    "Medical_Charges": [60000, 20000, 80000, 15000, 55000]
}

df = pd.DataFrame(data)

print("Patient Data:")
print(df)

# 1. Patients above 60 years
print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

# 2. Average medical charge
print("\nAverage Medical Charge:")
print(df["Medical_Charges"].mean())

# 3. Maximum medical charge
print("\nMaximum Medical Charge:")
print(df["Medical_Charges"].max())

# 4. Patients with charges greater than 50000
print("\nPatients with Medical Charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])