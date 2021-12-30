class Student:
    # Write here the constructor and methods of the class
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

    # The print statement or str() built-in function uses Object.__str__() to display the string representation of the object
    # ** Code **
    # def __str__(self):
    #     s = ""
    #     s += "\nFirst name: " + self.get_firstname()
    #     s += "\nLast name: " + self.get_lastname()
    #     s += "\nAge: " + str(self.get_age())
    #     s += "\nYear: " + self.get_year()
    #     return s

    def to_string(self):
        s = ""
        s += "\nFirst name: " + self.get_firstname()
        s += "\nLast name: " + self.get_lastname()
        s += "\nAge: " + str(self.get_age())
        s += "\nYear: " + self.get_year()
        return s
