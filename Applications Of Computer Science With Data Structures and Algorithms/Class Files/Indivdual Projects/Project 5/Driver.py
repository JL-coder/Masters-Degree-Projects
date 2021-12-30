from Stack import Stack

#Stacks need to be global since they have to work in two functions!
#Holds variables (numbers)
variable = Stack()
#Holds operands and parenthesis -> might need seperate space for paraenthesis
operands = Stack()

def main():
    print("Please type an arithmetic expression made from")
    print("unsigned numbers and the operations + - * / .")
    print("The expression must be fully parenthesized.")

    #Boolean flag to manage while loop. Will become false and shut off if the user does not want to input a new expression
    boolean_flag = True

    while boolean_flag:
        user_input = input("Your expression: ")

        #Break apart each char in string
        stack_input = [character for character in user_input]

        #Use map function on the user input and remove spaces so that it can be evaluated in the evaluate function
        #expression = map(str, user_input)
        #expression = ''.join(expression).split()

        #Checks if the inputted equation is balanced. If it is than the evaluate function is run. After its run it will display the result and pop off
        #  the result from the stack so that that stacks are cleared for the next run. If the equation is not balanced a warning message will be displayed.
        # Displayed value is limited to 2 decimal places
        if isBalanced(stack_input):
            a = evaluate(stack_input)
            #Assumes that all expressions are positive. So if the expression is illegal and -1 is returned then nothing gets printed. Otherwise the value is printed.
            if a != -1:
                print("The value is: ", round(a, 2))
                if variable.isEmpty() != True:
                    variable.pop()
            else:
                print("")
            
        else:
            print("The expression is not balanced!")
            print("")
        #Asks user if they want to input another string. Filters input into query function which handles the response
        yn_input = input("Another string? [Y or N]: ")
        boolean_flag = query(yn_input)

#This function handles the job of parsing the mathmatical string the user inputs. The function parses the string and adds variables and operands to their respective stacks and
#performs mathmatical operations on them by pushing these charachters to the evauateStackTops function. The results are pushed back to the stacks. When the string/stacks are parased
#the function will return the answer. If any part of the inputted equation is illegal i.e. 5+5+ or 9/0 than it will tell the user the expression is illegal and return -1.
def evaluate(expression):
    #Create a dictionary where the operand is the key and the value is how important that key is with regard to the mathamtical order of operations.
    precedence = {}
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    precedence["("] = 1
    precedence["{"] = 1
    precedence["["] = 1

    #Lists to check inputted values against
    open_par_list = ["[", "{", "("]
    closed_par_list = ["]", "}", ")"]
    operator_list = ['*', '/', '+', '-']

    #Counter variable to be used to help account for multi-digit numbers and floats
    counter = 0

    #print("Running evaluate function!")
    #Main for-loop runs through the length of the inputted expression and checks for parenthesis, numbers, and operands.
    for x in range(len(expression)):
        if counter >= 1:
            counter -= 1
            continue #Go back over and fix if I have time. Otherwise if it aint broke don't fix it.

        #Check if there is a number assign to a variable, if there is another number or "." then it will get concatenated to the variable and eventually pushed to the variable stack
        if expression[x] >= '0' and expression[x] <= '9':
            number = expression[x]
            #Check if there is consecutive numbers - counter will increase if there is.
            for y in range(x + 1, len(expression)):
                if (expression[y] >= '0' and expression[y] <= '9') or expression[y] == '.':
                    number = number + expression[y]
                    counter += 1
                else:
                    break #Again go back over and fix but I need to get SOMETHING running. Otherwise if it ain't broke don't fix it.
            variable.push(number)
        #Check for open parenthesis and push to operands stack if there are
        elif expression[x] in open_par_list:
            operands.push(expression[x])
        #Check for closed parenthesis
        elif expression[x] in closed_par_list:
            #While loop makes sure that the operands stack is not empty and that its top does not contain an open parenthesis 
            while (operands.isEmpty != True) and (operands.top() not in open_par_list):
                #Check the length of the variable stack and make sure it has more than two elements. If it does then run the evaluateStackTops function and push the result to the variable stack.
                #If the criteria are not met than the expression is illegal (can't perform an operation on a single variable). 
                #Also check the top of the variable stack for a 0 and operands stack for /. If it is the expression is illegal because the user is dividing by zero. 
                #Anytime the expression is illegal the stacks are cleared.
                if (variable.top() == '0' and operands.top() == '/'):
                    while operands.isEmpty() != True:
                        operands.pop()
                    while variable.isEmpty() != True:
                        variable.pop()
                    print("The expression is illegal")
                    return -1
                elif len(variable.getItems()) >= 2:
                    value = evaluateStackTops(variable, operands)
                    variable.push(str(value))
                else:
                    while operands.isEmpty() != True:
                        operands.pop()
                    while variable.isEmpty() != True:
                        variable.pop()
                    print("The expression is illegal")
                    return -1
            operands.pop()
        #If find an operator
        elif expression[x] in operator_list:
            #While loop checks that the operands list is not empty. That the top contains an open/closed parenthesis. Then checks for precedence of operators. After the while loop runs the stacks are run through
            # the evaluateStackTops function and the resulting value is pushed to the variable stack.
            while (operands.isEmpty() != True) and (precedence[operands.top()] >= precedence[expression[x]]) and (len(variable.getItems()) > 1):
                value = evaluateStackTops(variable, operands)
                print(value)
                variable.push(value)
            #Push operator into stack otherwise
            operands.push(expression[x])

    #At this point the stack should be parsed with paranethsis and some numbers evaluated. This will run at the end to evaluate any remaining numbers.
    #If the length of the variable/operand stack is 1 then the expression is illegal (cant perform an operation on a single variable and operand). Handles equations like (5+5)+
    #Also checks if the expression is trying to divide by 0 (in this case outside of parenthesis)
    while operands.isEmpty() != True:
        if (variable.top() == '0' and operands.top() == '/'):
            while operands.isEmpty() != True:
                    operands.pop()
            while variable.isEmpty() != True:
                    variable.pop()
            print("The expression is illegal")
            return -1
        elif ((len(variable.getItems()) == 1) and (len(operands.getItems()) == 1)):
            while operands.isEmpty() != True:
                    operands.pop()
            while variable.isEmpty() != True:
                    variable.pop()
            print("The expression is illegal")
            return -1
        variable.push(evaluateStackTops(variable, operands))
    
    #Returns the top of the processed variable stack
    return variable.top()

#Function performs mathmatical operations based on what numbers had pushed pushed to the variable and operands stack.
def evaluateStackTops(numbers, operation):
    #If the + sign is on top of the operations stack this will run. It assigns the top two numbers popped off the numbers stack to a variable,
    #  adds them, pops off the operand from the operations stack, and returns the result.
    if str(operation.top()) == '+':
        num1 = numbers.pop()
        num2 = numbers.pop()
        result = float(num1) + float(num2)
        operation.pop()
        return result
    #If the - sign is on top of the operations stack this will run. It assigns the top two numbers popped off the numbers stack to a variable,
    #  subtracts them, pops off the operand from the operations stack, and returns the result.
    elif str(operation.top()) == '-':
        num1 = numbers.pop()
        num2 = numbers.pop()
        result = float(num2) - float(num1)
        operation.pop()
        return result
    #If the * sign is on top of the operations stack this will run. It assigns the top two numbers popped off the numbers stack to a variable,
    #  multiplies them, pops off the operand from the operations stack, and returns the result.
    elif str(operation.top()) == '*':
        num1 = numbers.pop()
        num2 = numbers.pop()
        result = float(num1) * float(num2)
        operation.pop()
        return result
    #If the / sign is on top of the operations stack this will run. It assigns the top two numbers popped off the numbers stack to a variable,
    #  divides them, pops off the operand from the operations stack, and returns the result. However if the denominator is a zero the both the operations and the variable stack will be cleared,
    # The expression will be decleared illegal and -1 will be returned. 
    elif str(operation.top()) == '/':
        #Need to consider if dividing by zero
        num1 = numbers.pop()
        num1 = float(num1)
        num2 = numbers.pop()
        num2 = float(num2)
        result = float(num2) / float(num1)
        operation.pop()
        return result
    
#Function checks for a Y or N input from the user. If Y than it returns True. If N then False.
# If the user inputs anything else it will give a warning and ask the user to input again.
def query(user_yn_input):
    # Check user input after casefolding to make input lower case
    if user_yn_input.casefold() == 'y':
        print("")
        return True
    elif user_yn_input.casefold() == 'n':
        print("")
        print("All numbers are interesting")
        return False
    else:
        print('Invalid Response. Please type Y or N.')
        print("")
        # Ask for another user input and call the function again to check it
        user_input = input('Another string? [Y or N]: ')
        return query(user_input)

#Function checks if the inputted equation is balanced. Returns True if it is and False if not.
def isBalanced(expression):
    #parentheses lists to check the input against
    open_par_list = ["[", "{", "("]
    closed_par_list = ["]", "}", ")"]
    #Create a stack object
    stack = Stack()
    #Counter variable for keeping track of how many items are in the stack
    counter = 0
    #Loop through inputted expression and if it contains an open parentheses add it to the stack and increase the counter
    for char in expression:
        if char in open_par_list:
            stack.push(char)
            counter += 1
        #If the expression contains a closed parentheses get the position of the index of the char from the closed parantheses list
        elif char in closed_par_list:
            position = closed_par_list.index(char)
            #Check the length of the stack to make sure its length is greater than zero and compare the element
            #using the position and counter variables to access the parentheses list and stack at that index. Deincrement the counter and pop the item off stack if true.
            if (len(stack.getItems()) > 0) and (open_par_list[position] == (stack.getItems()[counter - 1])):
                counter -= 1
                stack.pop()
            else:
                return False
    #If the stack is found to be empty return True otherwise false
    if stack.isEmpty():
        return True
    else:
        return False

if __name__== "__main__":
    main()