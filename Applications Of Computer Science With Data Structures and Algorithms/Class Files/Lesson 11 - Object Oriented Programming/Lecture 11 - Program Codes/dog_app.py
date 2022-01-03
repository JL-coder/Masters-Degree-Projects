from Dog import Dog

def main():
    my_dog = Dog("Willie", 6)

    print("My dog's name is " + my_dog.get_name() + ".")
    print("My dog is " + str(my_dog.get_age()) + " years old.")
    my_dog.sit()

    your_dog = Dog("Lucy", 3)

    print()
    print("Your dog's name is " + your_dog.get_name() + ".")
    print("Your dog is " + str(your_dog.get_age()) + " years old.")
    your_dog.roll_over()

    another_dog = Dog()

    print()
    print("Another dog's name is " + another_dog.get_name() + ".")
    print("Another dog is " + str(another_dog.get_age()) + " years old.")
    another_dog.roll_over()

if __name__ == "__main__":
    main()