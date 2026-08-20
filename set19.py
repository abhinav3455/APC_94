morning = {"Amit", "Rahul", "Sneha", "Priya"}
afternoon = {"Sneha", "Priya", "Neha", "Karan"}

print("Both sessions:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one session:", morning | afternoon)