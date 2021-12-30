from Set import Set

def main():
    print()
    all = Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    odds = Set([1, 3, 5, 7, 9])
    evens = Set([2, 4, 6, 8, 10])
    print("all", all, "Size: ", all.getSize())
    print()
    print("all contains 10: ", all.contains(10))
    print()
    all.add(11)
    print("all adds 11: ", all)
    print()
    all.remove(11)
    print("all removes 11: ", all)
    print()
    print("odds is the subset of evens: ", odds.isSubsetOf(evens)) # **
    print()
    print("odds is equal to evens: ", odds.equal(evens)) # **
    print()
    print("all", odds.union(evens))
    print()
    print("all", evens.union(odds))
    print()
    print("odds", all.intersect(odds))
    print()
    print("odds", all.subtract(evens))

if __name__ == "__main__":
    main()