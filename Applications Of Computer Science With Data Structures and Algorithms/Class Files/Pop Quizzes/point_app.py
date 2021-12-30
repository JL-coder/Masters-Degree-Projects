from Point import Point

def main():
    x = int(input("X Coordinate: "))
    y = int(input("Y Coordinate: "))

    my_point = Point(x, y)
    print(my_point.toString() + "\n")

    xByOne = input("Increase X by one (Yes/No): ")
    if xByOne == "Yes":
        my_point.increaseOneOnX()

    yByOne = input("Increase Y by one (Yes/No): ")
    if yByOne == "Yes":
        my_point.increaseOneOnY()

    print(my_point.toString() + " after the increase.")

if __name__ == "__main__":
    main()