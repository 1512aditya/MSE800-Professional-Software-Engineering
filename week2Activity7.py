class HRdepartment:
    def display_info(self):
        print('Insert data for new employee\n')
        self.name = input("Enter the Employee name: ")
        self.salary = int(input("Enter the Salary: "))
        self.jobTitle = input("Enter the jobTitle: ")

        self.emp1 = [self.name, self.salary, self.jobTitle]
        self.emp2 = ['Adi', 800, 'Java Developer']
        self.emp3 = ['Aditya', 700, 'C++ Developer']

        print("\nEmployee Details:")
        print(f"Name: {self.emp1[0]}\nSalary: {self.emp1[1]}\nJob Title: {self.emp1[2]}")
        print(f"Name: {self.emp2[0]}\nSalary: {self.emp2[1]}\nJob Title: {self.emp2[2]}")
        print(f"Name: {self.emp3[0]}\nSalary: {self.emp3[1]}\nJob Title: {self.emp3[2]}")

    def give_raise(self):
        self.emp1rais = int(input("\nGive the raise to 1st employee: "))
        self.emp1[1] += self.emp1rais

        self.emp2rais = int(input("Give the raise to 2nd employee: "))
        self.emp2[1] += self.emp2rais

        self.emp3rais = int(input("Give the raise to 3nd employee: "))
        self.emp3[1] += self.emp3rais

        print('\nUpdated Employee Info:')
        print(f"Name: {self.emp1[0]}\nSalary: {self.emp1[1]}\nJob Title: {self.emp1[2]}")
        print(f"Name: {self.emp2[0]}\nSalary: {self.emp2[1]}\nJob Title: {self.emp2[2]}")
        print(f"Name: {self.emp3[0]}\nSalary: {self.emp3[1]}\nJob Title: {self.emp3[2]}")


def main():
    hr = HRdepartment()  
    hr.display_info()    
    hr.give_raise()      


if __name__ == '__main__':
    main()
