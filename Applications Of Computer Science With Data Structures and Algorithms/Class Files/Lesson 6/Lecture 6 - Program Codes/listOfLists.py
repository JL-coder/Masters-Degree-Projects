def numberOfNegative(listOfLists):
    cpt = 0
    for aList in listOfLists:
        for e in aList:
            if e < 0:
                cpt += 1
    return cpt

def main():
    my_list = [[-1, 2, 3, -4], [1, 4], [2, -5, 6, 7], [2, 3, 4, -1]] # Two dimensional List
    print(numberOfNegative(my_list))

if __name__ == "__main__":
    main()