def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks, max_marks_per_subject=10):
    total = calculate_total(marks)
    max_possible_marks = len(marks) * max_marks_per_subject
    if max_possible_marks == 0:
        return 0.0
    return (total / max_possible_marks) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    marks = [8, 9, 7, 10, 8]

    total = calculate_total(marks)
    percentage = calculate_percentage(marks, max_marks_per_subject=10)
    grade = calculate_grade(percentage)

    print("Total Marks:", total)
    print("Percentage:", f"{percentage:.2f}%")
    print("Grade:", grade)