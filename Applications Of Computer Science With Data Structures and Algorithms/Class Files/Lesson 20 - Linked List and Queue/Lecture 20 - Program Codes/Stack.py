class Stack:
    def __init__(self):
        self.__items = []

    def getItems(self):
        return self.__items

    def pop(self):
        if self.isEmpty():
            print("Attempt to pop an empty stack")
        else:
            topId = len(self.getItems())-1
            item = self.getItems()[topId]
            del self.getItems()[topId]
            return item

    def push(self, item):
        self.getItems().append(item)

    def top(self):
        if self.isEmpty():
            print("Attempt to get top of empty stack")
        else:
            topId = len(self.getItems())-1
            return self.getItems()[topId]

    def isEmpty(self):
        return len(self.getItems()) == 0