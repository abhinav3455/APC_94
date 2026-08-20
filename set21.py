python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Rahul", "Priya", "Neha", "Karan"}

both = python_students & java_students
only_one = python_students ^ java_students

print("Both courses:", both)
print("Only one course:", only_one)