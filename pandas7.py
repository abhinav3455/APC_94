import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "TV", "Keyboard", "Printer"],
    "Category": ["Electronics", "Electronics", "Electronics",
                 "Accessories", "Electronics"],
    "Price": [50000, 20000, 30000, 1500, 12000],
    "Quantity": [2, 3, 1, 10, 2]
}

df = pd.DataFrame(data)

# Add Total Sales column
df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Retail Sales Data:")
print(df)

print("\nProducts with Sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with Maximum Sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales:")
print(df["Total_Sales"].mean())