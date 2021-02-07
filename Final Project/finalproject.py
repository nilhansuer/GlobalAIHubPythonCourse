# Company Management System

print("*****MANAGER*****")
class Manager:
    def __init__(self, m_name, m_surname, m_age):
        self.manager_name = m_name
        self.manager_surname = m_surname
        self.manager_fullname = m_name + m_surname
        self.manager_age = m_age
    def printmanager_name(self):
        print(self.manager_name + self.manager_surname)
    def printmanager_age(self):
        print(self.manager_fullname + " is " + str(self.manager_age) + " years old.")
    def manager_status(self):
        print(self.manager_fullname + " is a manager and " + str(self.manager_age) + " years old.")

manager1 = Manager("Egehan", " Candan ", 30)
manager1.printmanager_name()
manager1.printmanager_age()
manager1.manager_status()

print(" ")
print("*****EMPLOYEE*****")


class Employees:
    def __init__(self, e_name, e_surname, e_age, e_languages):
        self.employees_name = e_name
        self.employees_surname = e_surname
        self.employees_fullname = e_name + e_surname
        self.employees_age = e_age
        self.employees_languages = e_languages
    def printemployees_name(self):
        print(self.employees_name + self.employees_surname)
    def printemployees_age(self):
        print(self.employees_name + " is " + str(self.employees_age) + " years old.")
    def employee_status(self):
        print(self.employees_fullname + " is an employee and " + str(self.employees_age) + " years old.")
    def printlanguages(self):
        print(self.employees_fullname + " can speak" + self.employees_languages)
employees1 = Employees("Nilhan", " Süer ", 20, " Turkish " + ", " + " English " + "and" + " Spanish .")
employees1.printemployees_name()
employees1.printemployees_age()
employees1.employee_status()
employees1.printlanguages()

print(" ")
print("*****EMPLOYEE'S LANGUAGES*****")

employees1.printlanguages()
