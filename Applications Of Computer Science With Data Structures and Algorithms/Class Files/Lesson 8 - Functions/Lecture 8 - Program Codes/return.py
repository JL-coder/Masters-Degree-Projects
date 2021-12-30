def averageWithPrint(x, y):
    print((x + y)/2)

def averageWithReturn(x, y):
    return ((x + y)/2) # return numerical values

def main():
    result1 = averageWithPrint(5, 2.5)
    print(result1)
    print(type(result1)) # NoneType is the type for the None object, which is an object that indicates no value.
                            # None is the return value of functions that "don't return anything".

    result2 = averageWithReturn(5, 2.5)
    print(result2)

if __name__ == "__main__":
    main()