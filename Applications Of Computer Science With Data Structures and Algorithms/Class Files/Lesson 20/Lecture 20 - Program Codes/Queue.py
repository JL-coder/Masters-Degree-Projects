class Queue:
    def __init__(self):
        self.__items = []

    def getItem(self):
        return self.__items

    def enqueue(self, item):
        self.getItem().append(item)

    def dequeue(self):
        if self.isEmpty():
            print("Attempt to dequeue an empty queue")
        else:
            item = self.getItem()[0]
            self.getItem().pop(0)
            return item

    def isEmpty(self):
        return len(self.getItem()) == 0

    def front(self):
        if self.isEmpty():
            print("Attempt to access front of empty queue")
        else:
            return self.getItem()[0]