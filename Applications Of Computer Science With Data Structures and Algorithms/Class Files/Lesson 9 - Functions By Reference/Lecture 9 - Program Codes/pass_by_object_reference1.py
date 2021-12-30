def main():
    int_var = 5
    returned_value = function_a(int_var)

    print(int_var is returned_value)
    print(int_var)
    print(returned_value)

# the int_var in this parameter is a different int_var that the one in main()
# the value of the pointer is copied, currently both int_vars are pointing to the address where 5 is stored

def function_a(int_var):
    int_var = 999  # reassign int_var (the one in the parameters) to point to a new memory location
    print("Inside function: " + str(int_var))
    return int_var

if __name__ == "__main__":
    main()