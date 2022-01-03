from Queue import Queue

def main():
    q = Queue()
    lst = list(range(10))
    lst2 = []

    for k in lst:
        q.enqueue(k) # Ascending Order

    if q.front() == 0:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")

    while not q.isEmpty():
        lst2.append(q.dequeue()) # Ascending Order

    if lst2 != lst:
        print("Test 2 Failed")
    else:
        print("Test 2 Passed")

if __name__=="__main__":
    main()