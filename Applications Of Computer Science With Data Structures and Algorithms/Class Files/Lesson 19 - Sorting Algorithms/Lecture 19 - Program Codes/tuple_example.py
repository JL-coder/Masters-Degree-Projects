def main():
    # CREATION #########################################################
    # create an empty tuple
    tuple1 = ()
    print("Tuple 1: ", tuple1)
    print(type(tuple1))
    print()

    tuple2 = tuple()
    print("Tuple 2: ", tuple2)
    print(type(tuple2))
    print()

    tuple3 = (1, 2, 3)
    print("Tuple 3: ", tuple3)
    print(type(tuple3))
    print()

    # ADD #############################################################
    tuple1 = tuple3 + tuple3
    print("Tuple 1: ", tuple1)
    print()

    # GET ############################################################
    print("GET")
    # get value for all keys and print out the string form
    print(str(tuple1[0]))
    print(str(tuple1[1]))
    print(str(tuple1[2]))
    print(str(tuple1[3]))
    print(str(tuple1[4]))
    print(str(tuple1[5]))

    print()

    # ITERATE ########################################################
    print("PRINT ALL VALUES IN TUPLE")

    for i in tuple1:
        print(str(i))

    # INCLUSION #######################################################
    # prints if given value is in the tuple
    print()
    print(1 in tuple1)

    # COUNT ###########################################################
    print()
    print(str(tuple1.count(1))) # Count the number of "1" in the tuple.


if __name__ == "__main__":
    main()