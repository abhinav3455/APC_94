students = {
    "Rahul": 75,
    "Amit": 92,
    "Sneha": 85
}

while True:
    print("\n1. Add student")
    print("2. Update marks")
    print("3. Delete student")
    print("4. Search student")
    print("5. Display all students")
    print("6. Find highest marks")
    print("7. Calculate average")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print(name, ":", students[name])
        else:
            print("Student not found")

    elif choice == 5:
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == 6:
        if students:
            name = max(students, key=students.get)
            print(name, ":", students[name])
        else:
            print("No students")

    elif choice == 7:
        if students:
            print("Average:", sum(students.values()) / len(students))
        else:
            print("No students")

    elif choice == 8:
        break

    else:
        print("Invalid choice")