class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject
    def print(self):
        print("Hello! I am " + self.name + ". I am in " + self.grade + " grade. My favorite subject is " + self.subject)

Vihaan = Student("Vihaan", "6th", "Math.")
Anvika = Student("Anvika", "3rd", "Science.")

Vihaan.print()
Anvika.print()