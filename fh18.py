def display():
    f = open("employees.txt", "r")
    for line in f:
        print(line, end="")
    f.close()

def highest_salary():
    f = open("employees.txt", "r")
    employees = []
    for line in f:
        id, name, dept, salary = line.strip().split(",")
        employees.append([id, name, dept, float(salary)])
    f.close()

    e = max(employees, key=lambda x: x[3])
    print("Highest Paid:", e[1], e[3])

def average_salary():
    f = open("employees.txt", "r")
    salaries = []
    for line in f:
        data = line.strip().split(",")
        salaries.append(float(data[3]))
    f.close()

    print("Average Salary:", sum(salaries) / len(salaries))

def above_salary(amount):
    f = open("employees.txt", "r")
    for line in f:
        data = line.strip().split(",")
        if float(data[3]) > amount:
            print(data)
    f.close()

f = open("employees.txt", "w")
f.write("101,Amit,IT,50000\n")
f.write("102,Priya,HR,60000\n")
f.write("103,Rahul,Sales,45000\n")
f.close()

display()
highest_salary()
average_salary()

amount = float(input("Enter salary: "))
above_salary(amount)