def sumFirstN(n):
    return n * (n+1) / 2

def main():
    x = int(input("Please enter a non-negative integer >= 0: "))
    s = sumFirstN(x)
    print("The sum of the first", x, "integers is", str(s)+".")

if __name__ == "__main__":
    main()