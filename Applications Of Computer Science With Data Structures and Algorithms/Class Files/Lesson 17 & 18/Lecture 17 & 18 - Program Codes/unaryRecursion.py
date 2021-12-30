def linearSum(A, n):            # STEP 1: Write the method header with the formal parameter(s).
    if n == 0:                  # STEP 2: Develop the code for the base case(s).
        return 0
    elif n == 1:                # STEP 2: Develop the code for the base case(s).
        return A[0]
    else:                       # STEP 3: Develop the code for the recursive case(s).
        return linearSum(A, n - 1) + A[n - 1]

# Suggested by your classmate, Abhinav. Great!
def linearSum(A):
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return A[0]
    else:
        return linearSum(A[1:]) + A[0]

def main():
    a = []
    x = input("Please enter a list of integers with a space: ")
    x = x.split(" ")
    for i in x:
        if bool(i):
            a.append(int(i))
    # print(linearSum(a, len(a)))
    print(linearSum(a))

if __name__ == "__main__":
    main()