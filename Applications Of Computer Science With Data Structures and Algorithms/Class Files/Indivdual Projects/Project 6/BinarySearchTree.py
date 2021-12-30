from Node import Node

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def getRoot(self):
        return self.__root

    def setRoot(self, node):
        self.__root = node

    def insertNode(self, val):
        node = Node(val)
        if self.getRoot() is None:
            self.setRoot(node)
        else:
            self.__insertNode(val, self.getRoot())

    def __insertNode(self, val, node): # Have you seen "==", why?
        if val < node.getVal() and node.getLeft() is not None:
            self.__insertNode(val, node.getLeft())
        elif val < node.getVal() and node.getLeft() is None:
            node.setLeft(Node(val))
        elif val > node.getVal() and node.getRight() is not None:
            self.__insertNode(val, node.getRight())
        elif val > node.getVal() and node.getRight() is None:
            node.setRight(Node(val))
        else:
            print("The same node is trying to be inserted.")

    def searchNode(self, val):
        # Base Cases: root is null or key is present at root
        if (self.getRoot() is None or self.getRoot().getVal() == val):
            return self.getRoot()

            # Key is greater than root's key
        elif val < self.getRoot().getVal():
            return self.__searchNode(val, self.getRoot().getLeft())

            # Key is smaller than root's key
        else:
            return self.__searchNode(val, self.getRoot().getRight())

    def __searchNode(self, val, node):
        if val == node.getVal():
            return node
        elif (val < node.getVal() and node.getLeft() is not None):
            return self.__searchNode(val, node.getLeft())
        elif (val > node.getVal() and node.getRight() is not None):
            return self.__searchNode(val, node.getRight())
        else:
            return "No Such Node."

    def printTree(self):
        if self.getRoot() is not None:
            self.__printTree(self.getRoot())
        else:
            print("The tree is empty.")

    def __printTree(self, node):
        if node is not None:
            self.__printTree(node.getLeft())
            print(str(node.getVal()) + " ")
            self.__printTree(node.getRight())

    def deleteTree(self):
        self.setRoot(None)

    def getTreeSize(self):
        if self.getRoot() is None:
            return 0
        else:
            return self.__getTreeSize(self.getRoot())

    def __getTreeSize(self, node):
        if node.getLeft() is None and node.getRight() is None:
            return 1
        elif node.getLeft() is None and node.getRight() is not None:
            return 1 + self.__getTreeSize((node.getRight()))
        elif node.getLeft() is not None and node.getRight() is None:
            return 1 + self.__getTreeSize((node.getLeft()))
        else:
            return 1 + self.__getTreeSize((node.getLeft())) + self.__getTreeSize((node.getRight()))

    def getLeftMostData(self):
        if self.getRoot() is None:
            return "No Left Most Data"
        else:
            return self.__getLeftMostData(self.getRoot())

    def __getLeftMostData(self, node):
        if node.getLeft() is None:
            return node.getVal()
        else:
            return self.__getLeftMostData(node.getLeft())

    def getRightMostData(self):
        if self.getRoot() is None:
            return "No Right Most Data"
        else:
            return self.__getRightMostData(self.getRoot())

    def __getRightMostData(self, node):
        if node.getRight() is None:
            return node.getVal()
        else:
            return self.__getRightMostData(node.getRight())

    def printLeafNode(self):
        res = ""

        if self.getRoot() is None:
            res += "No Leaf Nodes"
        else:
            res += self.__printLeafNode(self.getRoot()) + " "

        return res

    def __printLeafNode(self, node):
        if node.getLeft() is None and node.getRight() is None:
            return str(node.getVal())
        elif node.getLeft() is not None and node.getRight() is None:
            return self.__printLeafNode(node.getLeft())
        elif node.getLeft() is None and node.getRight() is not None:
            return self.__printLeafNode(node.getRight())
        else:
            return self.__printLeafNode(node.getLeft()) + " " + self.__printLeafNode(node.getRight())

    def preorderTrav(self):
        res = ""

        if self.getRoot() is None:
            res += "The tree is empty."
        else:
            res += self.__preorderTrav(self.getRoot())

        return res

    def __preorderTrav(self, node):
        res = ""
        if node is not None:
            res += str(node.getVal()) + " " #**#
            return res + self.__preorderTrav(node.getLeft()) + self.__preorderTrav(node.getRight())
        else:
            return res

    def inorderTrav(self):
        res = ""

        if self.getRoot() is None:
            res += "The tree is empty."
        else:
            res += self.__inorderTrav(self.getRoot())

        return res

    def __inorderTrav(self, node):
        res = ""

        if node.getLeft() is not None:
            res += self.__inorderTrav(node.getLeft())

        res += str(node.getVal()) + " " #**#

        if node.getRight() is not None:
            res += self.__inorderTrav(node.getRight())

        return res

    def postorderTrav(self):
        res = ""

        if self.getRoot() is None:
            res += "The tree is empty."
        else:
            res += self.__postorderTrav(self.getRoot())

        return res

    def __postorderTrav(self, node):
        res = ""

        if node.getLeft() is not None:
            res += self.__postorderTrav(node.getLeft())

        if node.getRight() is not None:
            res += self.__postorderTrav(node.getRight())

        res += str(node.getVal()) + " " #**#

        return res

    def levelorderTrav(self):
        list = []
        res = ""

        if self.getRoot() is None:
            return "The tree is empty."
        else:
            list.append(self.getRoot())
            self.__levelorderTrav(list, self.getRoot())

        for i in list:
            res += str(i.getVal()) + " "

        return res

    def __levelorderTrav(self, list, node):
        if node.getLeft() is not None:
            list.append(node.getLeft())

        if node.getRight() is not None:
            list.append(node.getRight())

        if node.getLeft() is not None:
            self.__levelorderTrav(list, node.getLeft())

        if node.getRight() is not None:
            self.__levelorderTrav(list, node.getRight())

    #Count number of leaves in a tree. Makes recursive calls to a private function of the same name. Otherwise returns zero if there is no tree.
    def countLeaves(self):
        if self.getRoot() is None:
            return 0
        else:
            return self.__countLeaves(self.getRoot())

    #Private recursive function that counts leave in the binary tree. 
    def __countLeaves(self, node):
        #If there are no left/right branches than return 1
        if (node.getLeft() is None) and (node.getRight() is None):
            return 1
        #If there is a left branch but not a right make a recursive call and continue moving down this branch.
        elif node.getLeft() is not None and node.getRight() is None:
            return self.__countLeaves((node.getLeft()))
        #If there is a right branch but not a left make a recursive call and continue moving down this branch.
        elif node.getLeft() is None and node.getRight() is not None:
            return self.__countLeaves((node.getRight()))
        #If there is a left and a right branch make a recursive call and continue down both branches adding up if there is a leaf.
        elif node.getLeft() is not None and node.getRight() is not None:
            return self.__countLeaves(node.getLeft()) + self.__countLeaves(node.getRight())

    #Count number of non-leaf nodes in a tree. IF there is no tree return 0 otherwise make recursive calls to a private function of the same name.
    def countNonLeaves(self):
        if self.getRoot() is None:
            return 0
        else:
            return self.__countNonLeaves(self.getRoot())
    
    #Private recursive function that counts non-leaves on a binary tree
    def __countNonLeaves(self, node):
        #If there is no left or right node than return 0
        if (node.getLeft() is None) and (node.getRight() is None):
            return 0
        #If there is a left node add 1 and continue down that branch
        elif node.getLeft() is not None and node.getRight() is None:
            return 1 + self.__countNonLeaves((node.getLeft()))
        #If there is a right node add 1 and continue down that branch
        elif node.getLeft() is None and node.getRight() is not None:
            return 1 + self.__countNonLeaves((node.getRight()))
        #If there is a left and right branch make recursive calls on both branches and add 1. 
        elif node.getLeft() is not None and node.getRight() is not None:
            return 1 + self.__countNonLeaves(node.getLeft()) + self.__countNonLeaves(node.getRight())
    
    #Function for getting the parent of a node inside the binary search tree class
    def getParent(self, node):
        return node.getParent()
    #Function for setting the parent of a node inside the binary search tree class
    def setParent(self, node):
        return node.setParent(node)

    #Function is supposed to print out the all of the parent nodes for each node branch
    def printParentNode(self):
        #Check if the tree is empty return a warning if it is
        if self.getRoot() is None:
            return "The tree is empty."
        #Otherwise declare the root node and set it to be the parent. Enter the private recursive function
        else:
            print(self.getRoot().getVal(), "is a root node.")
            self.setParent(self.getRoot())
            self.__printParentNode(self.getRoot())

    #Private print parent node function. Keeps track of the parents/children and prints them to the console
    def __printParentNode(self, node):
        #Check if the left node is not empty if it is not then print the parent of the node along with the node itself and set the new node as the parent
        if node.getLeft() is not None:
            print(self.getParent(node).getVal(), "is the parent of ", node.getLeft().getVal())
            self.setParent(node.getLeft())

        #Check if the right node is not empty if it is not then print the parent of the node along with the node itself and set the new node as the parent
        if node.getRight() is not None:
            print(self.getParent(node).getVal(), "is the parent of ", node.getRight().getVal())
            self.setParent(node.getRight())

        #Make a recursive call and move down the left branch
        if node.getLeft() is not None:
            self.__printParentNode(node.getLeft())

        #Make a recursive call and move down the right branch
        if node.getRight() is not None:
            self.__printParentNode(node.getRight())