


# 1. Problem Statement


import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(10, 4), Triangle(8, 6)]
for shape in shapes:
    print("Area:", round(shape.area(), 2))



# 2. Problem Statement


class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 80000 + 20000

class Developer(Employee):
    def calculate_salary(self):
        return 60000 + 10000

class Tester(Employee):
    def calculate_salary(self):
        return 50000 + 8000

employees = [Manager(), Developer(), Tester()]
for employee in employees:
    print("Salary:", employee.calculate_salary())



# 3. Problem Statement


class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button.")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with a large engine.")

vehicles = [Car(), Bike(), Bus()]
for vehicle in vehicles:
    vehicle.start()



# 4. Problem Statement


class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog: Bark")

class Cat(Animal):
    def sound(self):
        print("Cat: Meow")

class Cow(Animal):
    def sound(self):
        print("Cow: Moo")

class Lion(Animal):
    def sound(self):
        print("Lion: Roar")

animals = [Dog(), Cat(), Cow(), Lion()]
for animal in animals:
    animal.sound()


# 5. Problem Statement


class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email.")

class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS.")

class PushNotification(Notification):
    def send(self):
        print("Sending notification through Push Notification.")

notifications = [EmailNotification(), SMSNotification(), PushNotification()]
for notification in notifications:
    notification.send()


# 6. Problem Statement


class Student:
    def calculate_grade(self, marks):
        pass

class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 40:
            return "C"
        return "F"

class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 75:
            return "A"
        elif marks >= 55:
            return "B"
        elif marks >= 40:
            return "C"
        return "F"

class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 70:
            return "A"
        elif marks >= 50:
            return "B"
        elif marks >= 40:
            return "C"
        return "F"

students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for student in students:
    print("Grade:", student.calculate_grade(78))



# 7. Problem Statement


class BankAccount:
    def calculate_interest(self, balance):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.04

class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02

class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.07

accounts = [SavingsAccount(), CurrentAccount(), FixedDepositAccount()]
for account in accounts:
    print("Interest:", account.calculate_interest(100000))


# 8. Problem Statement


class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("Generating PDF report.")

class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report.")

class HTMLReport(Report):
    def generate(self):
        print("Generating HTML report.")

def generate_report(report):
    report.generate()

reports = [PDFReport(), ExcelReport(), HTMLReport()]
for report in reports:
    generate_report(report)



# 9. Problem Statement


class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet + total_inches // 12
        total_inches = total_inches % 12
        return Distance(total_feet, total_inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")

d1 = Distance(5, 8)
d2 = Distance(3, 9)
d3 = d1 + d2
d3.display()



# 10. Problem Statement


class StudentMarks:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        return self.total_marks < other.total_marks

s1 = StudentMarks("Abhinav", 450)
s2 = StudentMarks("Rahul", 420)

print("s1 > s2:", s1 > s2)
print("s1 < s2:", s1 < s2)



# 11. Problem Statement


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

p1 = Product("Laptop", 60000)
p2 = Product("Mobile", 30000)

print("Products have equal price:", p1 == p2)
print("Laptop is more expensive:", p1 > p2)



# 12. Problem Statement


class Payment:
    def make_payment(self, amount):
        pass

class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI payment of Rs.", amount, "successful.")

class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card payment of Rs.", amount, "successful.")

class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet payment of Rs.", amount, "successful.")

def process_payment(payment, amount):
    payment.make_payment(amount)

payments = [UPIPayment(), CardPayment(), WalletPayment()]
for payment in payments:
    process_payment(payment, 1500)


# 13. Problem Statement


class Person:
    def display_role(self):
        pass

class Student(Person):
    def display_role(self):
        print("Role: Student")

class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")

class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")

people = [Student(), Faculty(), Administrator()]
for person in people:
    person.display_role()


# 14. Problem Statement


class Media:
    def play(self):
        pass

class Audio(Media):
    def play(self):
        print("Playing audio.")

class Video(Media):
    def play(self):
        print("Playing video.")

class Podcast(Media):
    def play(self):
        print("Playing podcast.")

media_list = [Audio(), Video(), Podcast()]
for media in media_list:
    media.play()



# 15. Problem Statement


class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SmartDevice):
    def turn_on(self):
        print("Light is ON.")

    def turn_off(self):
        print("Light is OFF.")

class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is ON.")

    def turn_off(self):
        print("Fan is OFF.")

class AC(SmartDevice):
    def turn_on(self):
        print("AC is ON.")

    def turn_off(self):
        print("AC is OFF.")

class TV(SmartDevice):
    def turn_on(self):
        print("TV is ON.")

    def turn_off(self):
        print("TV is OFF.")

devices = [Light(), Fan(), AC(), TV()]
for device in devices:
    device.turn_on()
    device.turn_off()
