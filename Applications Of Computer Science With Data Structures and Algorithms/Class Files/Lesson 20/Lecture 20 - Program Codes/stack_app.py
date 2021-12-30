from Stack import Stack

def main():
    s = Stack()
    lst = list(range(10))
    print(id(lst))
    lst2 = []
    print(id(lst2))

    for k in lst:
        s.push(k) # Ascending Order

    if s.top() == 9:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")

    while not s.isEmpty():
        lst2.append(s.pop()) # Descending Order

    print()
    print("Before: ", lst2)
    lst2.reverse() # Function Provided by Lists
    print("After: ", lst2)
    print()

    print(id(lst2))
    print(id(lst))
    if lst2 != lst:
        print("Test 2 Failed")
    else:
        print("Test 2 Passed") # The two lists' content are the same.

if __name__=="__main__":
    main()