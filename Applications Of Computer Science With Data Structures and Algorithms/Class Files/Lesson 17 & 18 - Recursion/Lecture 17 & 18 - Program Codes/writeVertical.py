def writeVertical(n): # STEP 1: Write the method header with the formal parameter(s).
    if n < 10:         # STEP 2: Develop the code for the base case(s).
        print(n)
    else:                   # STEP 3: Develop the code for the recursive case(s).
        writeVertical(n//10) # Integer Division
        print(n%10) # Reminder Division

def main():
    x = int(input("Please enter a non-negative integer >= 0: "))
    writeVertical(x)

if __name__ == "__main__":
    main()