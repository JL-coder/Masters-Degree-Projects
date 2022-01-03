def main():
    # CREATION #########################################################
    # create an empty set
    set1 = set()
    print("Set 1: ", set1)
    print()

    # ADD #############################################################
    # add values to the set
    set1.add("A")
    set1.add("B")
    set1.add("C")
    set1.add("D")
    print("Set 1: ", set1) # Order Change After Each Execution
    print()

    set2 = set(["C", "D", "E", "F"]) # works fine, but below method
    set2 = {"C", "D", "E", "F", "F"}
    print("Set 2: ", set2) # Order Change After Each Execution

    # ITERATE ########################################################
    print()
    print("Set 1")

    # i is a value in the set
    for i in set1:
        # print out value for each key
        print(str(i))
    print()

    print("Set 2")

    # i is a value in the set
    for i in set2:
        # print out value for each key
        print(str(i))

    # INCLUSION #######################################################
    print()
    print("A" in set1)  # prints true or false
    print("A" not in set1) # prints true or false

    # UNION ###########################################################
    print()
    print("Union: " + str(set1 | set2))
    print("Union: " + str(set1.union(set2)))

    # INTERSECTION ####################################################
    print()
    print("Intersection: " + str(set1 & set2))
    print("Intersection: " + str(set1.intersection(set2)))

    # SET DIFFERENCE ##################################################
    print()
    print("Set difference: " + str(set1 - set2))
    print("Set difference: " + str(set1.difference(set2)))

    # SUBSET/SUPERSET#################################################
    print()
    print("Subset/superset: " + str(set1 > set2))
    print("Subset/superset: " + str(set1.issuperset(set2)))
    print("Subset/superset: " + str(set1.issubset(set2)))

    # DISJOINT #######################################################
    print()
    print("Disjoint: " + str(set1.isdisjoint(set2)))

    # UPDATE  #######################################################
    print()
    set1.update(set2)
    print("Update: " + str(set1)) #Add set2 content to set1

    # ADD  #######################################################
    print()
    set1.add("Z")
    print("Add: " + str(set1))  # Add an element content to set1

    # DISCARD/REMOVE ##########################################################
    print()
    set1.discard("A") #  If the element(argument) passed to the discard() method doesn't exist,
    # no exception is thrown
    print("Set 1: ", set1)
    print()
    set1.remove("B") # If the element(argument) passed to the remove() method doesn't exist,
    # keyError exception is thrown.
    print("Set 1: ", set1)

    # POP ##########################################################
    print()
    print("Pop: " + str(set1.pop())) # Remove an arbitrary element in Set 1

    # REMOVE ALL ######################################################
    print()
    set1.clear()
    print("Set 1: ", set1)

if __name__ == "__main__":
    main()