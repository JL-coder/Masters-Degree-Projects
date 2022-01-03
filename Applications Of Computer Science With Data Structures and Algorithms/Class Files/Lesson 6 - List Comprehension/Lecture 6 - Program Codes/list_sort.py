def main():
    my_list = [] # Create a new list object

    my_list1 = [1, 5, 3, 4, 2]
    print(my_list1)
    print(id(my_list1))

    my_list2 = [1, 5, 3, 4, 2]
    print(id(my_list2))

    my_list3 = [1, 5, 3, 4, 2]
    print(id(my_list3))
    print()

    print()

    my_list1.sort()
    print(my_list1)
    print((id(my_list1)))
    my_list3.sort(reverse=True)
    print(id(my_list3))


    print()
    print(my_list1)
    print(my_list2)
    print(my_list3)

if __name__ == "__main__":
    main()