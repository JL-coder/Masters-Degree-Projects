def main():
    filename = input("Please enter the name of a file: ")
    file = open(filename, "r")

    for line in file:
        print(line)
    file.close()

if __name__ == "__main__":
    main()