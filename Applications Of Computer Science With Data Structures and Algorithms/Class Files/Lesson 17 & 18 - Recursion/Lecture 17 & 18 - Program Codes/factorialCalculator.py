def calculateFactorial(n): # STEP 1: Write the method header with the formal parameter(s).
    if n == 0:             # STEP 2: Develop the code for the base case(s).
        return 1
    else:                       # STEP 3: Develop the code for the recursive case(s).
        n * calculateFactorial(n - 1)

def main():
    x = int(input("Please enter a non-negative integer >= 0 : "))
    s = calculateFactorial(x)
    print("The factorial of", x, "is", str(s) + ".")

if __name__ == "__main__":
    main()