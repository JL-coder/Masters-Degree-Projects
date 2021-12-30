class A:
    def __init__(self):
        print("A init")

    def function_a(self):
        print("A function a")


class B(A):
    def __init__(self):
        print("B init")
        # super().__init__()

    def function_a(self): # Overrided
        print("B function a")


class C(A):
    def __init__(self):
        print("C init")
        # super().__init__()

    def function_a(self): # Overrided
        print("C function a")


class D(B, C):
    def __init__(self):
        print("D init")
        # super().__init__()

    def function_a(self):
        print("D function a")

my_a = A()

my_b = B()

my_c = C()

my_d = D()

print(issubclass(A, B))
print(issubclass(B, A))

print(isinstance(my_a, A))
print(isinstance(my_b, A))

print(isinstance(my_a, B))
print(isinstance(my_b, B))

print(D.mro())
print(A.__subclasses__())
print(D.__bases__)

my_d.function_a()