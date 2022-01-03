def print_stars1(rows):
    for i in range(rows):
        star = ""
        for j in range(i + 1):
            star += "*"
        print(star)

def print_stars2(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end="")
        print()

def main():
    rows = int(input("Enter a number of rows to print out: "))
    # print_stars1(rows)
    print()
    print_stars2(rows)

if __name__ == "__main__":
    main()