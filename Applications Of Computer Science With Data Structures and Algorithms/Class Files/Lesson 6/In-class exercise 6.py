def main():
    #user_input = int(input("Please enter an integer greater than 1: "))
    #classExercise1(user_input)
    #printStars(5)
    my_list = [[-1,2,3,4], [1,4], [2,-5,6,7], [2,3,4,-1]]
    my_list2 = [[[1,2,3], [4,5,6],[7,8,9]], [[10,20,30], [40,50,60], [70,80,90]], [[19,29,39], [49,59,69], [79,89,99]]]
    #countNegativeElements(my_list)
    print3DList(my_list2)
def print3DList(threeDlist):
    for list in threeDlist:
        for sub_list in list:
            for element in sub_list:
                print(element, end = ",")
        print()

def countNegativeElements(listOfLists):
    count = 0
    for list in listOfLists:
        for element in list:
            if element < 0:
                count += 1
    print(count)

def classExercise1(n):
    result = str(n) + " "
    while (n > 1):
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        result += str(n)
        result += " "

def without_break():
    keep_looping = bool(input("Do you want to remain in this loop (Any String/null)?"))
    while keep_looping:
        keep_looping = bool()

def printStars(rows):
    for i in range(rows):
        star = ""
        for j in range(i + 1):
            star += "*"
        print(star)

if __name__ == "__main__":
    main()
