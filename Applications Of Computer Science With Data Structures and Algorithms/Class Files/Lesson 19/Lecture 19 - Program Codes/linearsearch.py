def linearsearch(list, value):
    for index in range(len(list)):
        if list[index] == value:
            return index

    return -1

def main():
    integer_list = [34, 56, 2, 10, 77, 51, 93, 30, 5, 52]
    searchvalue = int(input("Enter the search value: "))
    print("The index of the search value", searchvalue, "is", linearsearch(integer_list, searchvalue))

if __name__ == "__main__":
    main()