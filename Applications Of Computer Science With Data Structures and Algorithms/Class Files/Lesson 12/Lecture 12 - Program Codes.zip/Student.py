class Student:
    institute = "WPI" # Class Variables

    def __init__(self, fname, lname, age, year):
        self.__firstname = fname
        self.__lastname = lname
        self.__age = age
        self.__year = year

    def get_firstname(self):
        return self.__firstname

    def set_firstname(self, name):
        self.__firstname = name

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, name):
        self.__lastname = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_institute(self): # Class Getter **
        return Student.institute

    def set_institute(self, inst): # Class Setter **
        Student.institute = inst

    # The print statement and str() built-in function uses __str__ to display the string representation of the object

    # def __str__(self):
    #     s = "\nFirst name1: " + self.get_firstname()
    #     s += "\nLast name: " + self.get_lastname()
    #     s += "\nAge: " + str(self.get_age())
    #     s += "\nYear: " + self.get_year()
    #     return s

    def to_String(self):
        s = "\nFirst name: " + self.get_firstname()
        s += "\nLast name: " + self.get_lastname()
        s += "\nAge: " + str(self.get_age())
        s += "\nYear: " + self.get_year()
        return s