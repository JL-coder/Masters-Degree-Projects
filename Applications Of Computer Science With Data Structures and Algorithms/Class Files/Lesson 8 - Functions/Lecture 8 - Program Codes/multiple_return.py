def positive_negative_zero(number): # The function works correctly whether or not the argument passed in is an int or a float
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"
# Return the string object

def main():
    print(positive_negative_zero(5))
    print(positive_negative_zero(-2.5))
    print(positive_negative_zero(0))

if __name__ == "__main__":
    main()