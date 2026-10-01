import pandas as pd

# Read CSV file
df = pd.read_csv("weather.csv")

# 1. Find maximum temperature
print("Maximum Temperature:")
print(df["Temperature"].max())

# 2. Find minimum temperature
print("\nMinimum Temperature:")
print(df["Temperature"].min())

# 3. Calculate average temperature
print("\nAverage Temperature:")
print(df["Temperature"].mean())

# 4. Display records where temperature is above 35°C
print("\nRecords where Temperature is above 35°C:")
print(df[df["Temperature"] > 35])

# 5. Calculate city-wise average temperature
print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())