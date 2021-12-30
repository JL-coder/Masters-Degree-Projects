def syracuse(n):
    res = str(n) + " "
    while (n > 1):
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        res += str(n)
        res += " "

    print(res)

def main():
    number = int(input("Enter an integer >= 1: "))
    syracuse(number)

if __name__ == "__main__":
    main()