def binarysearch(integer_list, search_value):
    low = 0
    high = len(integer_list) - 1
    middle = (low + high + 1) // 2
    location = -1 # The search value has not been found yet.

    while(low <= high and location == -1):
        if search_value == integer_list[middle]:
            location = middle
        elif search_value < integer_list[middle]:
            high = middle - 1
        else:
            low = middle + 1

        middle = (low + high + 1) // 2

    return location

def main():
    integer_list = [2, 3, 5, 10, 27, 30, 34, 51, 56, 65, 77, 81, 82, 93, 99]
    search_value = int(input("Enter the search value: "))
    print("The index of the search value", search_value, "is", binarysearch(integer_list, search_value))

if __name__ == "__main__":
    main()