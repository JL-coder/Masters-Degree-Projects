def main():
    s = input("Please enter a list of integers: ")

    lst = s.split() # lst is a list of integer-like string objects
    print(lst)

    count = 0
    for e in lst:
        count = count + 1

    print("There were", count, "integers in the list.")

if __name__ == "__main__":
    main()