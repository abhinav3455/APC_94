import pandas as pd

products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}

s = pd.Series(products)

print("Products and Prices:")
print(s)

# Increase every price by 10%
s = s * 1.10

print("\nPrices after 10% increase:")
print(s)

print("\nMost Expensive Product:")
print(s.idxmax(), "=", s.max())

print("\nProducts costing more than 1000:")
print(s[s > 1000])