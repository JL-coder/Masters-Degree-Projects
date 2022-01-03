def main():
    # CREATION #########################################################
    # create an empty dictionary
    dictionary1 = {}
    print("Dict 1: ", dictionary1)
    print()

    # create a dictionary with initial key-value mappings
    dictionary2 = {"A": 1, "B": 2, "C": 3, "D": 4}
    print("Dict 2: ", dictionary2)
    print()

    # ADD #############################################################
    # add keys/values to the dictionary
    dictionary1["W"] = 1
    dictionary1["X"] = 2
    dictionary1["Y"] = 3
    dictionary1["Z"] = 4

    # SET #############################################################
    # set keys to different values
    dictionary1["W"] = 5
    dictionary1["X"] = 6
    dictionary1["Y"] = 7
    dictionary1["Z"] = 8

    # dictionary1["A"] = dictionary1.pop("W") # Change the Key Value
    print("Dict 1: ", dictionary1)
    print()

    # GET ############################################################
    print("GET")
    # get value for all keys and print out the string form
    print(str(dictionary2["A"]))
    # print(dictionary2.get("A"))
    print(str(dictionary2["B"]))
    print(str(dictionary2["C"]))
    print(str(dictionary2["D"]))
    print(str(dictionary1["W"]))
    print(str(dictionary1["X"]))
    print(str(dictionary1["Y"]))
    print(str(dictionary1["Z"]))

    print()

    # ITERATE ########################################################
    print("PRINT ALL VALUES IN DICTIONARY 2")

    # i is a KEY
    # will assign keys into i for each iteration
    for i in dictionary2:
        # print out value for each key
        print(str(dictionary2[i]))
    print()
    print(dictionary2.items()) # All the key-value pairs
    print(dictionary2.keys()) # All the keys only
    print(dictionary2.values()) # All the values only
    print()

    # INCLUSION #######################################################
    # prints if given key is in the dictionary
    print("A" in dictionary2)
    print()

    # DELETE/REMOVE Key-Value Pairs#####################################
    del dictionary1["W"]
    dictionary1.pop("X")
    print(dictionary1)
    print()

    # REMOVE ALL ######################################################
    dictionary2.clear()
    print(dictionary2)

if __name__ == "__main__":
    main()