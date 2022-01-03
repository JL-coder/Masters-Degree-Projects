from Node import Node

class LinkedList:
    def __init__(self):
        self.__head = Node(None, None)
        self.__tail = self.__head
        self.__numNodes = 1

    def getHead(self):
        return self.__head

    def setHead(self, node):
        self.__head = node

    def getTail(self):
        return self.__tail

    def setTail(self, node):
        self.__tail = node

    def getNumNodes(self):
        return self.__numNodes

    def setNumNodes(self, numNodes):
        self.__numNodes = numNodes

    def getNodeData(self, index):
        cursor = self.getHead()
        if index == 0:
            return cursor.getData()
        elif index > 0 and index < self.getNumNodes():
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getData()
        else:
            print("LinkedList Retrieval Index Out of Range")

    def setNodeData(self, index, val):
        cursor = self.getHead()
        if index == 0:
            return cursor.setData(val)
        elif index > 0 and index < self.getNumNodes():
            for i in range(index):
                cursor = cursor.getNext()

            cursor.setData(val)
        else:
            print("LinkedList Assignment Index Out of Range")

    def appendNewNode(self, data):
        node = Node(None)
        cursor = self.getTail()
        cursor.setNext(node)
        self.setTail(node)
        self.setNumNodes(self.getNumNodes() + 1)
        self.setNodeData(self.getNumNodes() - 1, data)

    def removeLastNode(self):
        if self.getNumNodes() == 0:
            print("LinkedList Removal Index Out of Range")
        elif self.getNumNodes() == 1:
            self.setHead(None)
            self.setTail(None)
            self.setNumNodes(self.getNumNodes() - 1)
        else:
            self.setNumNodes(self.getNumNodes() - 1)
            cursor = self.getHead()
            for i in range(self.getNumNodes()):
                if i == self.getNumNodes() - 1:
                    cursor.setNext(None)
                    self.setTail(cursor)
                else:
                    cursor = cursor.getNext()

    def insertNode(self, index, data):
        if index == 0:
            node = Node(data, self.getHead())
            self.setHead(node)
            self.setNumNodes(self.getNumNodes() + 1)

        elif index > 0 and index < self.getNumNodes():
            cursor = self.getHead()
            for i in range(index):
                if i == index - 1:
                    node = Node(data, cursor.getNext())
                    cursor.setNext(node)
                    self.setNumNodes(self.getNumNodes() + 1)
                else:
                    cursor = cursor.getNext()
        else:
            self.appendNewNode(data)

    def removeNode(self, index):
        if index == 0:
            self.setHead((self.getHead().getNext()))
            self.setNumNodes(self.getNumNodes() - 1)

        elif index > 0 and index < self.getNumNodes():
            cursor = self.getHead()
            for i in range(index):
                if i == index - 1:
                    nextNode = cursor.getNext()
                    cursor.setNext(nextNode.getNext())
                    self.setNumNodes(self.getNumNodes() - 1)
                else:
                    cursor = cursor.getNext()
        else:
            self.removeLastNode()

    def searchTargetData(self, searchTarget):
        cursor = self.getHead()
        for i in range(self.getNumNodes()):
            if cursor.getData() == searchTarget:
                return cursor
            else:
                cursor = cursor.getNext()

        return None

    def searchTargetIndex(self, searchIndex):
        if searchIndex < 0 or searchIndex > self.getNumNodes() - 1:
            print("No Such Index")
            return None
        else:
            cursor = self.getHead()
            for i in range(searchIndex + 1):
                if i == searchIndex:
                    return cursor
                else:
                    cursor = cursor.getNext()