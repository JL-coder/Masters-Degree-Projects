from Node import Node

class LinkedQueue:
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

    def isEmpty(self):
        return self.getNumNodes() == 0

    def front(self):
        if self.isEmpty():
            print("Cannot dequeue from an empty queue")
        else:
            return self.getHead().getData()


    #I completely froze on this I have no idea what I am doing pop quizzes make me nervous
    #Just give me a zero this isnt gonna work
    def enqueue(self, data):
        linkedq = LinkedQueue()
        cursor = self.getHead()
        tail = self.getTail()
        if self.isEmpty():
            linkedq.setHead(data)
        #Enter que from zero and continue adding to the back. Mind the cursor location. Set new tail each time and move cursor
        else:
            for x in range(len(self.getNumNodes())):
                #I know this wont work I cant think of anything more logical or functional that will let me parse this
                if x == tail:
                    #Need to move the cursor as we traverse the list...que thing 
                    tail = tail.getNext()
                    #Need to increase the size of the list
                    linkedq = linkedq.setNumNodes(self.getNumNodes + 1)
                    #Set the data into the new tail
                    linkedq = linkedq.setTail(data)
                    #Want to set the final node to none?
                    tail.setNext(None)
                    #Set new number nodes to the number that linkedq has?
                    self.setNumNodes(len(linkedq))
                else:
                    #Want to move down the line so set the tail to move to next
                    tail = tail.getNext()

                    


    def dequeue(self):
        #Dequeue happens from the front!
        linkedq = LinkedQueue()
        if self.isEmpty():
            print("Cannot dequeue from an empty queue")
        else:
            item = self.front()
            #Somehow remove item
        
