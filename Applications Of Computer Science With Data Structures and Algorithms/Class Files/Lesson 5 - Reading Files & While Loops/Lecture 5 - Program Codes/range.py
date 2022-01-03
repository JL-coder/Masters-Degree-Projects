def main():
    start = 1
    stop = 5
    thisRange = range(start, stop)
    print(thisRange)
    print(type(thisRange))  # An object of a Range class
    print()

    # start = 0, by default
    # stop = 11 (last element = 10)
    # increment = 1, by default
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(range(11))


    # start = 5
    # stop = 11 (last element = 10)
    # increment = 1, by default
    # [5, 6, 7, 8, 9, 10]
    print(range(5, 11))


    # start = 0
    # stop = 11 (last element = 10)
    # increment = 2
    # [0, 2, 4, 6, 8, 10]
    print(range(0, 11, 2))

    # start = 4
    # stop = 11 (last element = 10)
    # increment = 2
    # [4, 6, 8, 10]
    print(range(4, 11, 2))


    # start = 10
    # stop = -1 (last element = 0)
    # increment = -2
    # [10, 8, 6, 4, 2, 0]
    print(range(10, -1, -2))


# You CANNOT make the change on the elements of a range.

if __name__ == "__main__":
    main()