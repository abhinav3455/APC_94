def student_grade(m1, m2, m3, m4, m5):
    percentage = (m1 + m2 + m3 + m4 + m5) / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

m1 = float(input("Enter subject 1 marks: "))
m2 = float(input("Enter subject 2 marks: "))
m3 = float(input("Enter subject 3 marks: "))
m4 = float(input("Enter subject 4 marks: "))
m5 = float(input("Enter subject 5 marks: "))

percentage, grade = student_grade(m1, m2, m3, m4, m5)
print("Percentage:", percentage)
print("Grade:", grade)