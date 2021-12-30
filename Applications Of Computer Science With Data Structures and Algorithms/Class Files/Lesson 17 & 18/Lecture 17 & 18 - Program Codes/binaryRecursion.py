import math

def binarySum(A, i, n):         # STEP 1: Write the method header with the formal parameter(s).
    if n == 0:                  # STEP 2: Develop the code for the base case(s).
        return A
    elif n == 1:                # STEP 2: Develop the code for the base case(s).
        return A[i]
    else:                       # STEP 3: Develop the code for the recursive case(s).
         return binarySum(A, i, math.ceil(n/2)) + binarySum(A, i + math.ceil(n/2), math.floor(n/2))# return binarySum(A, i, n//2) + binarySum(A, i+n//2, n//2)

def main():
    a = []
    x = input("Please enter a list of integers with a space: ")
    x = x.split(" ")
    for i in x:
        if bool(i):
            a.append(int(i))
    print(binarySum(a, 0, len(a)))

if __name__ == "__main__":
    main()