# global_variable1 can be accessed by anything in the module after declaration
# can also be accessed by other modules

global_variable1 = 1

def main():
    # local_variable1 can be accessed by anything in the function after declaration
    local_variable1 = 2
    print(global_variable1) # Try global_variable1 and global_variable2
    print(local_variable1)

# print(local_variable1) # local_variable1 is not visible outside of the main() function

if __name__ == "__main__":
    main()

global_variable2 = 3