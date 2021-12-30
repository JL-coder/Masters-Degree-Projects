import math

def main():
    # Built-in Function
    result = abs(-11)
    print(result)
    result = pow(2, 3)
    print(result)
    print()

    # Non-Built-in Function
    result = math.gcd(4, 8)
    print(result)
    result = math.sqrt(2)
    print(result)
    print()

    # Functions in Classes
    my_string = "Test String"
    result = my_string.lower()
    print(result)
    print(type(result))

if __name__ == "__main__":
    main()