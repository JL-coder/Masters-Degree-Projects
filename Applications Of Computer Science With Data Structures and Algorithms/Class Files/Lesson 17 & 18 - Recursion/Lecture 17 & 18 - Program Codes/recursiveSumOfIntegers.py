def recSumFirstN(n):    # STEP 1: Write the method header with the formal parameter(s).
    if n == 0:          # STEP 2: Develop the code for the base case(s).
        return 0
    else:               # STEP 3: Develop the code for the recursive case(s).
        return recSumFirstN(n - 1) + n

def main():
    x = int(input("Please enter a non-negative integer >= 0: "))
    s = recSumFirstN(x)
    print("The sum of the first", x, "integers is", str(s) + ".")

if __name__ == "__main__":
    main()