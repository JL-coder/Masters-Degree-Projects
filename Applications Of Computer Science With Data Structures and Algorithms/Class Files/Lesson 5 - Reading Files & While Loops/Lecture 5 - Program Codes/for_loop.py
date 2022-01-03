def main():
    for i in range(10): # range object
        print(i)
    print()

    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: # list object
        print(i)
    print()

    for j in [3, "hello", 4.3, 3 + 3j, False]:
        print(j)
    print()

    for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9): # tuple object
        print(i)
    print()

    for j in (3, "hello", 4.3, 3 + 3j, False):
        print(j)
    print()

if __name__ == "__main__":
    main()