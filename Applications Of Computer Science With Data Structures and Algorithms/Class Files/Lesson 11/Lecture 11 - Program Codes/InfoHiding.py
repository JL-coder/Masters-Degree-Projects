# MUST SHOW: https://bhartidig.medium.com/access-modifiers-in-python-public-private-protected-fe5f923bd914

class InfoHiding:
    def __init__(self):
        self.visible = "Look at me" # public instance variable
        self._alsoVisible = "Look at me too" # protected instance variable
        self.__invisible = "Do not look at me directly" # private instance variable

    def print_visible(self): # public instance method
        print(self.visible)
        # self.__print_invisible() # public method can call it.

    def _print_also_visible(self): # protected instance method
        print(self._alsoVisible)
        # self.__print_invisible() # projected method can call it.

    def __print_invisible(self): # private instance method
        print(self.__invisible)

# For demo, I include the main() function here. NOT Recommended

def main():
    test = InfoHiding()
    print(test.visible)
    print(test._alsoVisible)
    # print(test.__invisible)

    print()
    test.print_visible()
    test._print_also_visible()
    # test.__print_invisible()

if __name__ == "__main__":
    main()