import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [1, 2, 3, 2, 1],
    "Price": [60000, 25000, 15000, 12000, 18000],
    "Discount": [5000, 2000, 1000, 500, 1000]
}

df = pd.DataFrame(data)

# Calculate Final Amount
df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest Value Order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage Order Value:")
print(df["Final_Amount"].mean())