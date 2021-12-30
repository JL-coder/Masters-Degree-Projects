def main():
    # start of main function block
    for i in range(10):
        # start of for loop block
        if i % 2 == 0:
            # start of if block
            print(str(i) + " is even")
            # end of if block
        else:
            # start of else block
            print(str(i) + " is odd")
            # end of else block
        # end of for loop block
        print("")
    # end of main function block

if __name__ == "__main__":
    main()