def main():
    # create a list with 5 elements
    my_list = [10, 20, 30, 40, 50]

    # len
    # print out the size of the list
    print(len(my_list))

    # slicing
    # print out the element at index 0
    print(my_list[0]) # 10

    # print out part of a list: Slicing
    print(my_list[0:2]) # [10, 20]
    print(my_list[1:4]) # [20, 30, 40]

    # append
    # append several elements to the end of the list
    for i in range(5):
        my_list.append(i)
    print(my_list)  # [10, 20, 30, 40, 50, 0, 1, 2, 3, 4]

    # append the second list to the end of the first lit
    my_list2 = [100, 200, 300, 400, 500]
    my_list.append(my_list2) # [10, 20, 30, 40, 50, 0, 1, 2, 3, 4, [100, 200, 300, 400, 500]]
    print(my_list)
    print(my_list[10][1]) # 200

    # extend
    my_list3 = [600, 700, 800, 900, 1000]
    my_list.extend(my_list3) # [10, 20, 30, 40, 50, 0, 1, 2, 3, 4, [100, 200, 300, 400, 500], 600, 700, 800, 900, 1000]
    print(my_list)

    # insert
    # insert an element at the beginning of the list
    my_list.insert(0, 99)
    print(my_list)  # [99, 10, 20, 30, 40, 50, 0, 1, 2, 3, 4, [100, 200, 300, 400, 500], 600, 700, 800, 900, 1000]

    # remove
    # remove "4" from the list (assuming it exists in the list)
    my_list.remove(4)
    print(my_list)  # [99, 10, 20, 30, 40, 50, 0, 1, 2, 3, [100, 200, 300, 400, 500], 600, 700, 800, 900, 1000]

    # del
    # delete the element at index 10
    del my_list[10]
    print(my_list)  # [99, 10, 20, 30, 40, 50, 0, 1, 2, 3, 600, 700, 800, 900, 1000]

    # sort
    # sort the list
    my_list.sort()  # Go to list_sort.py
    print(my_list) # Sort only integer and float or their combinations. [0, 1, 2, 3, 10, 20, 30, 40, 50, 99, 600, 700, 800, 900, 1000]

    my_string = "This is a test string from Andrew"
    my_string_list = my_string.split() # A list of string objects. ['This', 'is', 'a', 'test', 'string', 'from', 'Andrew']
    print(my_string_list)
    my_string_list.sort(key=str.lower, reverse=True) # ['This', 'test', 'string', 'is', 'from', 'Andrew', 'a']
    print(my_string_list)

    # index
    # search the list for "50"
    search_value = 50
    my_index = my_list.index(search_value)
    print("Found " + str(search_value) + " at index " + str(my_index))

    start = 2 # first index = start
    end = 9 # last index = end - 1, 9 is fine.
    my_index = my_list.index(search_value, start, end)
    print("Found " + str(search_value) + " at index " + str(my_index))

    # clear
    # clear the list
    my_list.clear()
    print(my_list)  # []

if __name__ == "__main__":
    main()