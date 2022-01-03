class Node:
    def __init__(self, data, node = None):
        self.__data = data
        self.__next = node

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getNext(self):
        return self.__next

    def setNext(self, node):
        self.__next = node