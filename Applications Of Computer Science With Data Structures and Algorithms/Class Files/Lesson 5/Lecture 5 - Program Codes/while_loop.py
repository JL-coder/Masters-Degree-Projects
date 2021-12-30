def example1():
    # for loop
    # for i in range(10):
    #    print(i)
    # equivalent while loop

    i = 0
    while i < 10:
        print(i)
        i = i + 1

# example borrowed and modified from our Python Programming book

def example2():
    # continue to ask user for values
    _sum = 0.0 # Accumulator
    count = 0 # Accumulator

    number = float(input("Enter a number or -1 to stop: "))

    while number != -1:
        _sum += number
        count += 1
        number = float(input("Enter a number or -1 to stop: "))

     # A sentinel loop is a loop that is controlled by a sentinel, which is a particular value to terminate the loop.

    print()
    print("Sum = " + str(_sum))
    print("Count = " + str(count))
    print("Average = " + str(_sum / count))

def main():
    example1()
    print()
    example2()

if __name__ == "__main__":
    main()