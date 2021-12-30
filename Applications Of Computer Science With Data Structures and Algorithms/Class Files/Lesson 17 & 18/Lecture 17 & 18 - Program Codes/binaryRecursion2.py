def fibonacci(k):               # STEP 1: Write the method header with the formal parameter(s).
    if k == 0 or k == 1:        # STEP 2: Develop the code for the base case(s).
        return k
    else:                       # STEP 3: Develop the code for the recursive case(s).
        return fibonacci(k - 1) + fibonacci(k - 2)

def main():
    x = int(input("Please enter a non-negative integer >= 0: "))
    s = fibonacci(x)
    print("The value of the", x, "Fibonacci number is", str(s)+".")

if __name__ == "__main__":
    main()