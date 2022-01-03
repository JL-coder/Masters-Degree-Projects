def printEven1(aList):
    res = ""
    for e in aList:
        if e % 2 == 0:
            res += str(e)
            res += " "

    print(res)  # Print them all on the same line as a string object

def printEven2(aList):
    res = []
    for e in aList:
        if e % 2 == 0:
            res.append(e)

    print(res)  # Print them all on the same line as a List object

def main():
    thisList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    printEven1(thisList)
    print()
    printEven2(thisList)

if __name__ == "__main__":
    main()