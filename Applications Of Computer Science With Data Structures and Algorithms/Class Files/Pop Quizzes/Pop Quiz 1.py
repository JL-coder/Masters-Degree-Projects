def main():
    boolean_flag = True
    while boolean_flag:
        x = int(input("Enter the first Number: "))
        y = int(input("Enter the second Number: "))
        if x == 0 and y == 0:
            print()
            print("Both numbers are zero!")
            boolean_flag = False
        elif (x + y) > 200:
            print("Sum = ", float(x + y), "*")
            print("Product = ", float(x * y))
            print("Average = ", float(((x + y) / 2)))
        else:
            print("Sum = ", float(x + y))
            print("Product = ", float(x * y))
            print("Average = ", float(((x + y) / 2)))
if __name__ == "__main__":
    main()