# NOT RECOMMENDED FOR MULTIPLE CLASSES IN THE SAME FILE. It is just for the demo.
class Employee1:
    def __init__(self, name, salary):
        self.name=name  # public instance attribute NOT Recommended
        self.salary=salary # public instance attribute NOT Recommended

class Employee2:
    def __init__(self, name, salary):
        self.__name=name  # private instance attribute Highly Recommended
        self.__salary=salary # private instance attribute Highly Recommended

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getSalarly(self):   # public instance methods
        return self.__salary

    def __getSalarly(self): # private instance methods
        return self.__salary

    def setSalarly(self, salary):  # public instance methods
        self.__salary = salary

    def __setSalarly(self, salary):  # private instance methods
        self.__salary = salary

def main():
    e1=Employee1("Ben", 10000)
    print(e1.salary)

    e1.salary=20000
    print(e1.salary)

    e2=Employee2("Ben", 10000)
    #print(e2.__salary)
    print(e2.getSalarly())

    # e2.__salary=20000
    # print(e2.__salary)

    e2.setSalarly(20000)
    print(e2.getSalarly())

if __name__ == "__main__":
    main()