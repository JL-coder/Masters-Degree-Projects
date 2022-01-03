def one_way(number):
    if number % 2 == 0:
        print("Your number is even.")

def two_way(number):
    if number % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

def multi_way(number):
    if number % 4 == 0:
        print("Your number is divisible by four.")
    elif number % 3 == 0:
        print("Your number is divisible by three.")
    elif number % 2 == 0:
        print("Your number is divisible by two.")
    else:
        print("Your number is not divisible by two, three, or four.")

def multi_conditions(number): # multiple comparisons
    if (number % 4 == 0) and (number % 3 == 0):
        print("Your number is divisible by four, three, and two.")
    elif (number % 3 == 0) and (number % 2 == 0):
        print("Your number is divisible by three and two.")
    elif number % 2 == 0:
        print("Your number is divisible by two.")
    else:
        print("Your number is not divisible by two, three, or four.")

def main():
    number = int(input("Enter a number: \n"))
    # one_way(number)
    # two_way(number)
    multi_way(number)
    # multi_conditions(number)

if __name__ == "__main__":
    main()