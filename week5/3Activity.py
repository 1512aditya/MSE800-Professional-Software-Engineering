class Person:
    def __init__(self, name, address, age, ID):
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID

    def display_info(self):
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Age: {self.age}")



class Student(Person):
    def __init__(self, name, address, age, ID, academic_record):
        super().__init__(name, address, age, ID)
        self.academic_record = academic_record

    def display_info(self):
        super().display_info()
        print(f"Academic Record: {self.academic_record}")


class AcademicStaff(Person):
    def __init__(self, name, address, age, ID, tax_code, salary):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Tax Code: {self.tax_code}")
        print(f"Salary: {self.salary}")


class GeneralStaff(Person):
    def __init__(self, name, address, age, ID, tax_code, pay_rate):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def display_info(self):
        super().display_info()
        print(f"Tax Code: {self.tax_code}")
        print(f"Pay Rate: {self.pay_rate}")

def main():
    student = Student("Alice", "123 Street", 20, "S001", "A+ in MSE")
    academic = AcademicStaff("Prof. ABC", "4 Nile road", 45, "A001", "TX123", 75000)
    staff = GeneralStaff("Charlie", "9 Road", 35, "G001", "TX456", 25.5)

    # Displaying information
    print("\nStudent Details")
    student.display_info()

    print("\nAcademic Staff Details")
    academic.display_info()

    print("\nGeneral Staff Details")
    staff.display_info()


if __name__ == "__main__":
    main()
    