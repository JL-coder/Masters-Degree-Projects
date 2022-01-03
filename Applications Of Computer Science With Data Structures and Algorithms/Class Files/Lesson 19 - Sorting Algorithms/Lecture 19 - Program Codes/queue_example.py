def main():
    queue = ["a", "b", "c", "d"]
    queue.append("e") # enqueue(e)
    queue.append("f") # enqueue(f)
    print(queue)
    queue.pop(0)
    print(queue)

if __name__ == "__main__":
    main()