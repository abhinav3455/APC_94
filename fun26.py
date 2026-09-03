def calculate_units_charge(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return 100 * 1.5 + (units - 100) * 2.5
    elif units <= 500:
        return 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        return 100 * 1.5 + 100 * 2.5 + 300 * 4 + (units - 500) * 6

def fixed_charge():
    return 100

def calculate_tax(amount):
    return amount * 0.05

def calculate_discount(amount):
    if amount > 5000:
        return amount * 0.10
    return 0

def final_electricity_bill(units):
    energy = calculate_units_charge(units)
    fixed = fixed_charge()
    subtotal = energy + fixed
    tax = calculate_tax(subtotal)
    discount = calculate_discount(subtotal)

    return subtotal + tax - discount

units = float(input("Enter units: "))
print("Final Bill:", final_electricity_bill(units))