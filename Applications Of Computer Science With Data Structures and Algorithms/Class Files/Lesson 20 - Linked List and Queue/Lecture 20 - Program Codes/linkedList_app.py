from LinkedList import LinkedList

def main():
    # [3, 7, 5, 12]
    # Head and Tail

    linkedlist = LinkedList()
    print("Head and Tail")
    print(linkedlist.getHead().getData())
    print(linkedlist.getTail().getData())
    print(linkedlist.getNumNodes())
    print()

    print("Set and Get Data")
    linkedlist.getHead().setData(4)
    linkedlist.getTail().setData(4)
    linkedlist.setNodeData(0, 4)
    print(linkedlist.getNodeData(0))
    print(linkedlist.getHead().getData())
    print(linkedlist.getTail().getData())
    print()

    linkedlist.setNodeData(0, 3)
    print(linkedlist.getNodeData(0))
    print(linkedlist.getHead().getData())
    print(linkedlist.getTail().getData())
    print()

    # Append New Nodes at the end of the List
    print("Append New Nodes")
    linkedlist.appendNewNode(7)
    linkedlist.appendNewNode(5)
    linkedlist.appendNewNode(12)
    print(linkedlist.getNumNodes())
    print(linkedlist.getNodeData(0))
    print(linkedlist.getNodeData(1))
    print(linkedlist.getNodeData(2))
    print(linkedlist.getNodeData(3))
    print(linkedlist.getHead().getData())
    print(linkedlist.getHead().getNext().getData())
    print(linkedlist.getTail().getData())
    print(linkedlist.getTail().getNext())
    print()

    # Remove the Last Node at the end of the List
    print("Remove the Last Node")
    linkedlist.removeLastNode()
    print(linkedlist.getNumNodes())
    print(linkedlist.getHead().getData())
    print(linkedlist.getTail().getData())
    print()

    # Insert a Node at Index = 1
    print("Insert a Node at Index = 1")
    linkedlist.insertNode(1, 4)
    print(linkedlist.getNumNodes())
    print(linkedlist.getNodeData(0))
    print(linkedlist.getNodeData(1))
    print(linkedlist.getNodeData(2))
    print(linkedlist.getNodeData(3))
    print(linkedlist.getHead().getData())
    print(linkedlist.getTail().getData())
    print()

    # Remove a Node at index 2
    print("Remove a Node at Index = 2")
    linkedlist.removeNode(2)
    print(linkedlist.getNumNodes())
    print(linkedlist.getNodeData(0))
    print(linkedlist.getNodeData(1))
    print(linkedlist.getNodeData(2))
    print()

    # Search a Node with its Value 4
    print("Search a Node with its Value 4")
    print(linkedlist.searchTargetData(4).getData())
    print(linkedlist.searchTargetIndex(1).getData())

if __name__ == "__main__":
    main()