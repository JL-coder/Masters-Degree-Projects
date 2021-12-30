from LinkedQueue import LinkedQueue

def main():
    q = LinkedQueue()
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst2 = []

    for k in lst:
        q.enqueue(k) # Ascending Order

    if q.front() == 0:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")

    while not q.isEmpty():
        lst2.append(q.dequeue()) # Ascending Order

    print()

    if lst2 != lst:
        print("Test 2 Failed")
    else:
        print("Test 2 Passed")

if __name__=="__main__":
    main()