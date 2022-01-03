def main():
    filename = input("Please enter the name of a file: ")
    your_name = input("What is your name? ")
    age = int(input("How old are you? "))

    file = open(filename, "w")
     # Create the new file automatically
    file.write("Hello " + your_name + ". How are you?\n")
    file.write("Next year you will be " + str(age + 1) + " years old\n")
    file.close()


if __name__ == "__main__":
    main()