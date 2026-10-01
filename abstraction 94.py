# ABSTRACTION - PYTHON PROGRAMS

from abc import ABC, abstractmethod


# Problem 1


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

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
    print("Area:", shape.area())



# Problem 2

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")

class Bike(Vehicle):
    def start(self):
        print("Bike started.")

    def stop(self):
        print("Bike stopped.")

class Bus(Vehicle):
    def start(self):
        print("Bus started.")

    def stop(self):
        print("Bus stopped.")

vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()


# Problem 3

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Savings balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings balance:", self.balance)
        else:
            print("Insufficient balance.")

class CurrentAccount(BankAccount):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance.")

savings = SavingsAccount(10000)
savings.deposit(2000)
savings.withdraw(3000)

current = CurrentAccount(15000)
current.deposit(5000)
current.withdraw(4000)


# Problem 4


class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 0

class HomeDeliveryOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 50

orders = [RestaurantOrder(), HomeDeliveryOrder()]

for order in orders:
    total = order.calculate_bill() + order.delivery_charge()
    print("Total Bill:", total)


# Problem 5

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass

class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient treatment provided.")

class OutPatient(Patient):
    def calculate_bill(self):
        return 1500

    def treatment(self):
        print("Out-patient treatment provided.")

class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 8000

    def treatment(self):
        print("Emergency treatment provided.")

patients = [InPatient(), OutPatient(), EmergencyPatient()]

for patient in patients:
    patient.treatment()
    print("Bill:", patient.calculate_bill())


# Problem 6

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2

class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5

class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 15

class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 10

transports = [Bus(), Train(), Taxi(), Flight()]

for transport in transports:
    print("Fare:", transport.calculate_fare(100))


# Problem 7

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass

class MCQQuestion(Question):
    def evaluate_answer(self, answer):
        if answer == "B":
            return "Correct"
        return "Wrong"

class TrueFalseQuestion(Question):
    def evaluate_answer(self, answer):
        if answer == "True":
            return "Correct"
        return "Wrong"

class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer):
        if len(answer) >= 20:
            return "Answer accepted"
        return "Answer too short"

questions = [
    MCQQuestion(),
    TrueFalseQuestion(),
    DescriptiveQuestion()
]

print(questions[0].evaluate_answer("B"))
print(questions[1].evaluate_answer("True"))
print(questions[2].evaluate_answer("This is a descriptive answer."))


# Problem 8

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using password.")

class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP.")

class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using biometric.")

methods = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for method in methods:
    method.authenticate()


# Problem 9

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive.")

    def download_file(self):
        print("File downloaded from Google Drive.")

    def delete_file(self):
        print("File deleted from Google Drive.")

class Dropbox(CloudStorage):
    def upload_file(self):
        print("File uploaded to Dropbox.")

    def download_file(self):
        print("File downloaded from Dropbox.")

    def delete_file(self):
        print("File deleted from Dropbox.")

storage_services = [GoogleDrive(), Dropbox()]

for storage in storage_services:
    storage.upload_file()
    storage.download_file()
    storage.delete_file()


# Problem 10

class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass

class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked.")

    def calculate_fee(self):
        return 500

class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked.")

    def calculate_fee(self):
        return 1000

class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked.")

    def calculate_fee(self):
        return 1500

appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

for appointment in appointments:
    appointment.book_appointment()
    print("Fee:", appointment.calculate_fee())
