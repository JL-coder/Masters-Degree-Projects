class A():
    def __init__(self, var_a=-1):
        # super().__init__()
        self.__var_a = var_a

    def getVar_a(self):
        return self.__var_a

    def setVar_a(self, var_a):
        self.__var_a = var_a


class B(A):
    def __init__(self, var_a, var_b):
        # super().__init__(var_a)
        A.__init__(self, var_a)
        self.__var_b = var_b

    def getVar_b(self):
        return self.__var_b

    def setVar_b(self, var_b):
        self.__var_b = var_b

my_a = A()
my_b = B(1, 2)

print(my_a.getVar_a())

print(my_b.getVar_a())

print(my_b.getVar_b())

print(issubclass(B, A))

print(isinstance(my_a, B))

print(A.__bases__)

print(A.__subclasses__())
#The prefix '__main__' appears in front of '.B' because I executed the code above in a python file.
# That is where the class B is defined.