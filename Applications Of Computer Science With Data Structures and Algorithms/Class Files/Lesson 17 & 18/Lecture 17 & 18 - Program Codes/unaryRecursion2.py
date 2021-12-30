def reverseList(A, i, j):          # STEP 1: Write the method header with the formal parameter(s).
    if i >= j:                      # STEP 2: Develop the code for the base case(s).
        return A
    else:                           # STEP 3: Develop the code for the recursive case(s).
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        return reverseList(A, i + 1, j - 1)

def main():
    a = []
    x = input("Please enter a list of integers with a space: ")
    x = x.split(" ")
    for i in x:
        if bool(i):
            a.append(int(i))
    print("Original List: ", a)
    print("New List: ", reverseList(a, 0, len(a)-1))

if __name__ == "__main__":
    main()