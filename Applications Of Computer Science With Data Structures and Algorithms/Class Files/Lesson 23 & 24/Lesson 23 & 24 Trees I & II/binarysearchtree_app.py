from BinarySearchTree import BinarySearchTree

def main():
    # 1. Testing Functions
    print("1. Testing Functions")
    tree = BinarySearchTree()
    tree.printTree()
    print()
    tree.insertNode(3)
    tree.insertNode(4)
    tree.insertNode(0)
    tree.insertNode(8)
    tree.insertNode(2)
    print("The number of nodes in the tree: ", str(tree.getTreeSize()))
    tree.printTree()
    print()
    print(tree.searchNode(3).getVal())
    print(tree.searchNode(10))
    print()
    print("The value at the left-most node of the tree: ", str(tree.getLeftMostData()))
    print("The value at the right-most node of the tree: ",str(tree.getRightMostData()))
    print()
    print("The values of all the leaf nodes of the tree: ", tree.printLeafNode())
    print()
    print("The values in the Preorder Traversal on the tree: ", tree.preorderTrav())
    print()
    print("The values in the Inorder Traversal on the tree: ", tree.inorderTrav())
    print()
    print("The values in the Postorder Traversal on the tree: ", tree.postorderTrav())
    print()
    print("The values in the Levelorder Traversal on the tree: ", tree.levelorderTrav())
    print()
    tree.deleteTree()
    tree.printTree()

    print()
    # 2. Testing Functions
    print("2. Testing Functions")
    s = input("Enter a list of numbers: ")
    lst = s.split()
    print()
    tree = BinarySearchTree()
    for x in lst:
        tree.insertNode(float(x))

    tree.printTree()

if __name__ == "__main__":
    main()