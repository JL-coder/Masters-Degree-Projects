class Dog:
    # No Constructor Overloading # Only Constructor Overriding
    def __init__(self, name, age):
        # a special method, object constructor, to create a new dog instance based on the Dog class.
        # Provide initial values for the instance variables of the object.

        self.__name = name # self is a reference parameter of the dog instance
        self.__age = age

    def __init__(self):
        # a special method, object constructor, to create a new dog instance based on the Dog class.
        # Provide initial values for the instance variables of the object.

        self.__name = "Peter" # self is a reference parameter of the dog instance
        self.__age = 8

    def __init__(self, name = None, age = None):
        # a special method, object constructor, to create a new dog instance based on the Dog class.
        # Provide initial values for the instance variables of the object.
        if name is None:
            self.__name = "Peter"
        else:
            self.__name = name

        if age is None:
            self.__age = 8
        else:
            self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.get_name() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(str(self.get_name()) + " rolled over!")