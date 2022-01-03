def bubblesort(integer_list):
    swap = True
    length = len(integer_list)

    while (swap and length >= 2):
        swap = False
        for i in range(length - 1):
            if integer_list[i] > integer_list[i + 1]:
                temp = integer_list[i]
                integer_list[i] = integer_list[i + 1]
                integer_list[i + 1] = temp
                swap = True

def main():
    integer_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubblesort(integer_list)
    print(integer_list)

if __name__ == "__main__":
    main()