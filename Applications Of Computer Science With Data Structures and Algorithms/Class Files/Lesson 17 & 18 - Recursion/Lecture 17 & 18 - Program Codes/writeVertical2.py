def writeVertical2(n):         # STEP 1: Write the method header with the formal parameter(s).
    if n >= 0 and n < 10: # STEP 2: Develop the code for the base case(s).
        print(n)
    elif n < 0:                # STEP 3: Develop the code for the recursive case(s).
        print("-")
        writeVertical2(-n)
    else:                           # STEP 3: Develop the code for the recursive case(s).
        writeVertical2(n//10)
        print(n%10)


def main():
    x = int(input("Please enter an integer: "))
    writeVertical2(x)

if __name__ == "__main__":
    main()