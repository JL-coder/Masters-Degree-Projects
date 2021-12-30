def main():
    stack = ["a", "b", "c", "d"]
    stack.append("e") # push(e)
    stack.append("f") # push(f)
    print(stack)
    stack.pop()
    print(stack)

if __name__ == "__main__":
    main()