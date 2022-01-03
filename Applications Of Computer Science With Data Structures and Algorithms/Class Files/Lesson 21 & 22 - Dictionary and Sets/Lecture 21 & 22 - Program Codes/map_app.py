from Map import Map

def main():
    # Add the entries to the map
    map = Map()
    map.add("A", 1)
    map.add("B", 2)
    map.add("C", 3)
    map.add("D", 4)
    print("The number of entry in the map: ", map.getNumberOfEntries())
    print(map)
    print()

    # Add the entry with the same key, "A"
    map.add("A", 5)
    print(map)
    print()

    # Remove the entry with the key, "C"
    map.remove("C")
    print("The number of entry in the map: ", map.getNumberOfEntries())
    print(map)
    print()

    # Remove the entry with the same key, "C"
    map.remove("C")
    print(map)
    print()

    # Get the value of the key, "A"
    print(map.valueOf("A"))
    print()

    # Get the value of the key, "C"
    print(map.valueOf("C"))
    print()

    # Update the value of the key, "A"
    print(map.updateValue("A", 5))
    print(map)
    print()

    # Update the value of the key, "C"
    print(map.updateValue("C", 1))
    print(map)

if __name__ == "__main__":
    main()