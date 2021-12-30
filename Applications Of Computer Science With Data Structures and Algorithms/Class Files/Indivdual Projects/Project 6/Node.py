class Node:
    def __init__(self, val, left=None, right=None, parent =None):
        self.__val = val
        self.__left = left
        self.__right = right
        self.__parent = parent

    def getVal(self):
        return self.__val

    def setVal(self, newVal):
        self.__val = newVal

    def getLeft(self):
        return self.__left

    def setLeft(self, newLeft):
        self.__left = newLeft

    def getRight(self):
        return self.__right

    def setRight(self, newRight):
        self.__right = newRight

    #Getter method for finding the parent of a node
    def getParent(self):
        return self.__parent
    #Setter method for setting the value of the parent node
    def setParent(self, newParent):
        self.__parent = newParent
