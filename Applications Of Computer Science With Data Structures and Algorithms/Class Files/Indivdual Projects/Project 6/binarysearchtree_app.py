from BinarySearchTree import BinarySearchTree

#Prints the root node twice. The second time it prints it is wrong. Not stopping sometimes -- dont know why

def main():

   boolean_flag = True
   print("")

   #While loop for handling user inputs
   while boolean_flag:

       #Create a binary tree
       b_tree = BinarySearchTree()

       #Input for the user. All input are converted to lower case. Will continue asking the user for input.
       user_input = input("Are you creating another tree? Enter yes/no to continue/quit. ").casefold()
       
       #If the user enters "yes" then the user will be able to create a tree and its output is printed otherwise if the user prints "no" then exits the application.
       #  Any other input causes the original question to repeat
       if user_input == "yes":
           b_tree = createBinaryTree()
           printBinaryTree(b_tree)
       elif user_input == "no":
            print("")
            print("Thank you for using my application")
            boolean_flag = False
       else:
            user_input = input("Are you creating another tree? Enter yes/no to continue/quit. ").casefold()

#Function creates a binary tree it also asks the user for node values    
def createBinaryTree():
    #Create binary tree object
    b_tree = BinarySearchTree()

    #Allows entry to into the while loop
    boolean_flag = True

    #Continuous while loop for inputting new nodes. 
    while boolean_flag:

        #Input asking the user for more nodes. All inputs turned to lower case
        input_more_nodes = input("Add more nodes? Enter yes/no to continue/quit. ").casefold()        
        
        #If the user inputs yes then it asks the user to input the node value, if no then it exits the loop
        if input_more_nodes == "yes":
            input_node = int(input("Please enter one node value at a time. Enter a node value: "))

            #Insert the inputted node into the tree.
            b_tree.insertNode(input_node)

        elif input_more_nodes == "no":
            boolean_flag = False
        
    return b_tree

#Function that prints out the current contents of the tree
def printBinaryTree(b_tree):
    print("")

    #Print ancestor nodes
    b_tree.printParentNode()
    #Print the leaves and non-leaves
    print("")
    print("The number of leaves of this tree is: ", b_tree.countLeaves())
    print("")
    print("Thyese number of non-leaves of this tree is: ", b_tree.countNonLeaves())
    print("")

if __name__ == "__main__":
    main()