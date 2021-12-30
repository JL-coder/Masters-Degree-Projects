def insertionsort(integer_list):
    length = len(integer_list)

    for i in range(1, length):
        insert = integer_list[i]
        moveitem = i
        while (moveitem > 0 and integer_list[moveitem - 1] > insert):
            integer_list[moveitem] = integer_list[moveitem - 1]
            moveitem = moveitem - 1

        integer_list[moveitem] = insert

def main():
    integer_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionsort(integer_list)
    print(integer_list)

if __name__ == "__main__":
    main()