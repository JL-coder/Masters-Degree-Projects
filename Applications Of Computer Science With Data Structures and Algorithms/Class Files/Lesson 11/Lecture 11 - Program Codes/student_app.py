from Student import Student
from CS5007 import CS5007

def main():
    student_list = []
    peter = Student("Peter", "Pan", 18, "Junior")
    student_list.append(peter)

    mary = Student("Mary", "Lau", 20, "Senior")
    student_list.append(mary)

    print(peter)
    print(peter.to_string()) # Polymorphism

    print()
    group = CS5007(student_list, "Ben Ngan", "Fall2021")
    print(group) # Print the memory address pointing to that object, as "group" is not a string object.
    print("**Ben Ngan**") # Pring **Ben Ngan**, as it is an string object.
    print()
    print(group.to_string()) # Polymorphism

    print()
    ben = Student("Ben", "Ngan", 28, "Masters")
    group.add_student(ben)
    print(group.to_string()) # Polymorphism

    print()
    group.remove_student(peter)
    print(group.to_string()) # Polymorphism

    print()
    david = Student("David", "Ngan", 29, "PhD")
    group.remove_student(david)
    print()
    print(group.to_string()) # Polymorphism

if __name__ == "__main__":
    main()