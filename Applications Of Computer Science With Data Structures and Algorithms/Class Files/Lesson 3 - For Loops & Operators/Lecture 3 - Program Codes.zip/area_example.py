import math

def main():
    # string --> int, float, complex, and bool
    outer = float(input("Enter the radius of the outer circle: "))
    inner = float(input("Enter the radius of the inner circle: "))
    # math.pi, the mathematical constant π = 3.141592…, to available precision.

    area = outer ** 2 * math.pi - inner ** 2 * math.pi

    """
    round(value, ndigits) returns the floating point number rounded off to the given ndigits digits 
    after the decimal point. If no ndigits is provided, it rounds off the number to the nearest integer.
    """

    print()

    print("The area of the part between the inner circle and the outer circle is ", area)
    print("The area of the part between the inner circle and the outer circle is ", round(area, 4))

if __name__ == "__main__":
    main()