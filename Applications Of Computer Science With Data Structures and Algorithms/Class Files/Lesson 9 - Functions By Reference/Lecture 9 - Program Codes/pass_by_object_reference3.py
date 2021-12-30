def main():
    list_var = [1, 2, 3, 4, 5]
    returned_value = function_a(list_var)

    print(list_var is returned_value)
    print(list_var)
    print(returned_value)

# the list_var in this parameter is a different list_var that the one in main()
# the value of the pointer is copied
# currently both list_vars are pointing to the address where the list values are stored

def function_a(list_var):
    list_var[0] = 999  # change what list_var contains for element zero of the list
    # NOTE, since lists are MUTABLE, the value in the list changes
    # both list_vars still point to the same list, a new list is not created
    print("Inside function: " + str(list_var))
    return list_var

if __name__ == "__main__":
    main()