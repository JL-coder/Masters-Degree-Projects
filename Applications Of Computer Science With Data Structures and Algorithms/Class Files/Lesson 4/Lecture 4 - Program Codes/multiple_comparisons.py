# unchained
def multiple_comparisons1():
    input_value = int(input("Enter a number\n"))
    if (input_value >= 0) and (input_value <= 10):
        print("You number (" + str(input_value) + ") is between 0 and 10 inclusively")

# chained
def multiple_comparisons2():
    input_value = int(input("Enter a number\n"))
    if 0 <= input_value <= 10:
        print("You number (" + str(input_value) + ") is between 0 and 10 inclusively")

def main():
    multiple_comparisons1()
    multiple_comparisons2()

if __name__ == "__main__":
    main()