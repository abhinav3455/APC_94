import pandas as pd

ages = {
    "P101": 65,
    "P102": 45,
    "P103": 70,
    "P104": 30,
    "P105": 62
}

s = pd.Series(ages)

print("Patient Ages:")
print(s)

print("\nAverage Age:")
print(s.mean())

print("\nOldest Patient:")
print(s.idxmax(), "=", s.max())

print("\nYoungest Patient:")
print(s.idxmin(), "=", s.min())

print("\nPatients above 60 years:")
print(s[s > 60])