from Student import Student

class PaidStudent(Student):
    def __init__(self, fname, lname, age, year, salary):
        Student.__init__(self, fname, lname, age, year)

        # super().__init__(fname, lname, age, year)

        # A special function helps Python make connections between the parent and child class.
        # This line tells Python to call __init__() method from Student class, which gives the PaidStudent object
        # all the attributes of its parent class.

        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def to_String(self):
        s = Student.to_String(self)
        s += ("\nSalary = " + str(self.get_salary()))
        return s