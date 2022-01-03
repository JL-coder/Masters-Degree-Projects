from PaidStudent import PaidStudent

def main():
    peter = PaidStudent("Peter", "Pan", 18, "Junior", 2000)
    paul = PaidStudent("Paul", "Wan", 20, "Senior", 2500)

    print(peter.to_String()) # Polymorphism
    print(peter.get_institute() + " == " + paul.get_institute())

    print(paul.to_String()) # Polymorphism
    #The value for the class applies to anyone!
    paul.set_institute("Worcester P.I.")
    print(peter.get_institute() + " == " + paul.get_institute())

if __name__ == "__main__":
    main()