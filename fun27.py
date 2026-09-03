def consultation_charges(amount):
    return amount

def laboratory_charges(amount):
    return amount

def medicine_charges(amount):
    return amount

def room_charges(amount):
    return amount

def discount(category, amount):
    if category == "senior":
        return amount * 0.10
    elif category == "child":
        return amount * 0.05
    return 0

def final_bill(consultation, laboratory, medicine, room, category):
    total = (
        consultation_charges(consultation)
        + laboratory_charges(laboratory)
        + medicine_charges(medicine)
        + room_charges(room)
    )

    return total - discount(category, total)

consultation = float(input("Consultation charges: "))
laboratory = float(input("Laboratory charges: "))
medicine = float(input("Medicine charges: "))
room = float(input("Room charges: "))
category = input("Patient category: ")

print("Final Bill:", final_bill(
    consultation,
    laboratory,
    medicine,
    room,
    category
))