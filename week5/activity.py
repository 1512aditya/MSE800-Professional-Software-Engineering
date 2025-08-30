class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'B'     # private

    def get_grade(self):
        return self.__grade
    
    # New method that uses private attribute
    def promote_student(self):
        print (self.__grade)
        

# New class to demonstrate public and protected attribute usage
class Course(Student):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course   # public

    def display_info(self):
        # Using public attribute (self.name) and protected attribute (self._age)
        return f"Graduate Student: {self.name}, Age: {self._age}, course: {self.course}"


# --- Example usage ---
def main():
    
    s = Student("Ali", 20)
    print(s.name)              # public -> accessible
    print(s._age)              # protected -> discouraged, but still accessible
    print(s.get_grade())       # correct way for private attribute
    print(s.promote_student()) # new method using private attribute

    c = Course("Adi", 22, "Python")
    print(c.display_info())    # using public + protected attributes

if __name__ == '__main__':
    main()
