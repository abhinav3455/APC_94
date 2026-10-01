import pandas as pd

data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [50000, 25000, 1500, 12000, 800],
    "Quantity": [2, 4, 10, 5, 20]
}

df = pd.DataFrame(data)

print("Product Data:")
print(df)

# Calculate Total Amount
df["Total_Amount"] = df["Price"] * df["Quantity"]

print("\nProduct Data with Total Amount:")
print(df)

# Product having highest total sales
print("\nProduct having Highest Total Sales:")
print(df.loc[df["Total_Amount"].idxmax()])