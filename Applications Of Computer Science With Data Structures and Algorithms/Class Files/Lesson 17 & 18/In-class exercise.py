import math
def fibonacci(k):
    if k == 0 or k == 1:
        return k
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)

def binarySum(A, i, n):
    if n == 0:
        return A
    elif n == 1:
        return A[i]
    else:
        return(A, i, math.ceil(n/2) + binarySum(A, i + math.ceil(n/2), math.floor(n/2)))

def reversedList(A, i, j):
    if i >= j:
        return A
    else:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        return reversedList(A, i + 1, j - 1)

def recursiveSumFirstN(n):
    if n == 0:
        return 0
    else:
        return recursiveSumFirstN(n - 1) + n

def factorial(n):
    if n == 0:
        return 1
    else:
        n * factorial(n - 1)
def writeVertical(n):
    if n < 10:
        print(n)
    else:
        writeVertical(n//10) #Integer Division
        print(n%10) #Reminder Division
def writeVertical2(n):
    if n >= 0 and n < 10:
        print(n)
    elif n < 0:
        print("-")
        writeVertical2(-n)
    else:
        writeVertical2(n//10)
        print(n%10)
def linearSum(A, n):
    if n == 0: #Multiple base cases
        return 0
    elif n == 1:
        return A[0]
    else:
        return linearSum(A, n - 1) + A[n - 1]
def main():
    x = int(input("Input a non-negative integer: "))
    s = recursiveSumFirstN(x)
    t = factorial(x)
    print("Sum of N" + str(s))
    print("Factorial of integer" + str(t))
if __name__ == "__main__":
    main()