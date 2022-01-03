def selectionsort(integer_list):
    length = len(integer_list)

    for i in range(length):
        smallest = i
        for index in range(i+1, length):
            if integer_list[index] < integer_list[smallest]:
                smallest = index

        if smallest != i:
            temp = integer_list[i]
            integer_list[i] = integer_list[smallest]
            integer_list[smallest] = temp

def main():
    integer_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selectionsort(integer_list)
    print(integer_list)

if __name__ == "__main__":
    main()
