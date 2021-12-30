# function for dividing and calling merge function
def mergesort(integer_list):
    n = len(integer_list)

    if (n >= 2):
        mid = n // 2
        left = []
        right = []

        for i in range(mid):
            number = integer_list[i]
            left.append(number)

        for i in range(mid, n):
            number = integer_list[i]
            right.append(number)

        mergesort(left)
        mergesort(right)
        merge(left, right, integer_list)

def merge(left, right, integer_list):
    i, j, k = 0, 0, 0

    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            integer_list[k] = left[i]
            i = i + 1
        else:
            integer_list[k] = right[j]
            j = j + 1
        k = k + 1

    while (i < len(left)):
        integer_list[k] = left[i]
        i = i + 1
        k = k + 1

    while (j < len(right)):
        integer_list[k] = right[j]
        j = j + 1
        k = k + 1

def main():
    integer_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergesort(integer_list)
    print(integer_list)

if __name__ == "__main__":
    main()