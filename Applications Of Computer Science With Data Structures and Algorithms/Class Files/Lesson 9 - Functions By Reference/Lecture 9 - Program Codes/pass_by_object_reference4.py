def main():
    list_var = [5, [6]]
    returned_value = function_a(list_var)

    print(list_var is returned_value)
    print(list_var)
    print(returned_value)

# the list_var in this parameter is a different list_var that the one in main()
# the value of the pointer is copied
# currently both list_vars are pointing to the address where the list values are stored

def function_a(list_var):
    new_list = list_var[:] # A new list object created with the same element objects
    new_list[0] = -1
    print(new_list[1][0])
    new_list[1][0] = -2
    return new_list

if __name__ == "__main__":
    main()