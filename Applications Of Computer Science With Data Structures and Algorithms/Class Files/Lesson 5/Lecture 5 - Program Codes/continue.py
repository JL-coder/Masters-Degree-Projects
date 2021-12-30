def with_continue():
    for i in range(10):
        if i == 5:
            continue
        print(i)

def without_continue():
    for i in range(10):
        if i != 5:
            print(i)

def main():
    # with_continue()
    without_continue()

if __name__ == "__main__":
    main()