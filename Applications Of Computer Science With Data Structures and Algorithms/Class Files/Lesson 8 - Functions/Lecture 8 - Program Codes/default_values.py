def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)

def main():
    greet("Kate")
    print()
    greet("Bruce", "How do you do?")

if __name__ == "__main__":
    main()