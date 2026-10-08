class InvalidMarksError(Exception):
    pass


name = input("Enter student name: ")
marks = int(input("Enter marks (0-10): "))

try:
    if marks < 0 or marks > 10:
        raise InvalidMarksError("Marks must be between 0 and 10.")

    print("Student Name:", name)
    print("Marks:", marks)

except InvalidMarksError as e:
    print("Error:", e)
