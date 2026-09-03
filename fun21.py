def total_bill(prices, quantities, discount):
    total = 0

    for price, quantity in zip(prices, quantities):
        total += price * quantity

    return total - (total * discount / 100)

prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))
discount = float(input("Enter discount percentage: "))

print("Total Bill:", total_bill(prices, quantities, discount))