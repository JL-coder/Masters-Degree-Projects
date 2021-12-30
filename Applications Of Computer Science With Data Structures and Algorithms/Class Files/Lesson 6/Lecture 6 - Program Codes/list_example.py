def main():
    my_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[10, 20, 30], [40, 50, 60], [70, 80, 90]],
               [[19, 29, 39], [49, 59, 69], [79, 89, 99]]]

    # i = list
    for i in my_list:
        # j = list
        for j in i:
            # k = integer value
            for k in j:
                print(k, end=",")
        print()

if __name__ == "__main__":
    main()