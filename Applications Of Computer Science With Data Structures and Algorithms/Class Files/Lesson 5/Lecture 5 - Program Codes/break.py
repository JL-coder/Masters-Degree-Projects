def with_break():
    while True:
        keep_looping = bool(input("Do you want to remain in this loop (Any String/null)? "))
        if not keep_looping:
            break

def without_break():
    keep_looping = bool(input("Do you want to remain in this loop (Any String/null)? "))
    while keep_looping:
        keep_looping = bool(input("Do you want to remain in this loop (Any String/null)? "))

def main():
    # with_break()
    without_break()

if __name__ == "__main__":
    main()