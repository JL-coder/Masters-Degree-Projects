def main():
    # Example List
    #hello = "bonjour"
    #thislist = [3, "hello", hello, 4.3, 3, 3 + 3, False]
    #print(thislist[3])
    #thislist[3] = 4.2
    #print(thislist[3])
    #print(type(thislist))

    # Example Tuple
    #thistuple = (3, "hello", hello, 4.3, 3, 3 + 3, False)
    #print(thistuple[3])

    # Example list/accumulator
    #s = input("Please enter a list of integers: ")
    #lst = s.split()  # Splits into indivdual string objects
    #print(lst)

    #count = 0
    #for e in lst:
    #   count += 1
    #print("There were ", count, " integers in the list.")

    #In-class exercise
    #user_input = int(input("Please enter a sequence of integers."))
    #input_list = []
    #even_num_list = []
    #input_list.append(user_input)
    #for x in input_list:
        #if x % 2 == 0:
            #even_num_list.append[x]
#thisList = [1,2,3,4,5,6,7,8,9]
#def printtEven2(aList):
    #res = []
    #for e in aList:
        #if e % 2 == 0:
            #res.append[e]
#def printEven1(aList):
    #res = ""
    #for x in aList:
        #if x % 2 == 0:
            #res += str(x)
            #res += " "

    #print(res)

def example2():
    sum = 0.0 #accumulator
    count = 0 #accumulator
    number = float(input("Enter a number or -1 to stop: "))
    while number != -1:
        sum += number
        count += 1
        number = float(input("Enter a number or -1 to stop: "))

if __name__ == "__main__":
    main()

