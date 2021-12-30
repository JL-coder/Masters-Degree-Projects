def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    result1 = power(num1, num2)  # positional arguments

    result2 = power(number=num1, power_=num2)  # keyword arguments
    result3 = power(power_=num1, number=num2)  # keyword arguments

    result4 = power(num1, power_=num2)  # both positional followed by keyword arguments

    print()
    print(result1)
    print(result2)
    print(result3)
    print(result4)

def power(number, power_):
    return pow(number, power_)

if __name__ == "__main__":
    main()