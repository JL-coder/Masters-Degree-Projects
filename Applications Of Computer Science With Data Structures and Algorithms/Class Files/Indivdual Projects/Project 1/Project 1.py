def main():
    #Variables for keeping track of the number of students, number of inputs, and user score inputs.
    student_count = 1
    index_list = []
    score_list = []
    index = 0

    user_input_score_loop(student_count, score_list, index_list, index)

    #After the function is run the while loop is initiated using a boolean switch that will be used to start and stop the loop.
    # It will ask if there are anymore students whose scores need to be inputted. If so the previous function is run again.
    # If not the loop is broken out of and the function for finding the average student scores (and min/ max of scores) for each student is run.

    user_yn_input = True
    while user_yn_input != "no":
        print()
        user_yn_input = str(input("Any more students? (Yes or No): ")).casefold()
        print()
        if user_yn_input == "yes":
            student_count += 1
            user_input_score_loop(student_count, score_list, index_list, index)
    find_mean_max_min(score_list, index_list)

#Function takes in student number, list of scores, list of index, and index. The function outputs the score and index
#list. The purpose of the function is to ask the user for the students score which is stored in the score_list. The
# number of scores inputted is stored in the index list. Any input that is not an float/integer will produce a notification
# and have you input numbers again. In order to break out of the loop the code -1 must be inputted by the user.
def user_input_score_loop(student_count, score_list, index_list, index):
    #Boolean switch for starting and stopping the while loop
    score_boolean_flag = True

    #User input is within a try/except block to handle error exceptions and give notifications of wrong input types
    while score_boolean_flag:
        try:
            user_num_input = float(input("Please enter Student %d's score (-1: Exit): " % student_count))
            if user_num_input == -1:
                index_list.append(index)
                score_boolean_flag = False
            score_list.append(user_num_input)
            index += 1

            #Quality check to make sure that the -1 input is not included in the score list.
            if -1 in score_list:
                score_list.remove(-1)
        except ValueError:
            print("The score entered is not a number. Please enter it again.")
            print("")
    return(score_list, index_list)

#Function tells us the mean, max, and min of the students scores based on the submitted score list and index list. The
# index list is used to slice into the score list and retrieve the correct set of numbers which are stored in a brand
# new list. This new list is then used when getting the mean, max, min.
def find_mean_max_min(scoreList, indexList):

    #counter for identifying students
    counter = 1

    # Create a new nested list broken down by each students inputs. Loops through the ranged length
    # of the index list. The expression sums and accesses index list at initial and next point to create a slice in the
    # score list and adds that slice to a new empty list
    new_list = [scoreList[sum(indexList[:i]):sum(indexList[:i + 1])] for i in range(len(indexList))]

    #Checks for any empty nested lists if there are any it defaults the mean, min, and max to zero for that entry.
    # Otherwise prints the mean, max, and mix for what is contained in the list.
    for element in new_list:
        if len(element) != 0:
            print("Student", counter, "took", len(element), "exams.")
            print("Average Score:", round((sum(element) / len(element)), 2))
            print("Highest Score:", max(element))
            print("Lowest Score:", min(element))
            print()
            counter += 1
        else:
            print("Student", counter, "took", 0, "exams.")
            print("Average Score:", 0)
            print("Highest Score:", 0)
            print("Lowest Score:", 0)
            print()
            counter += 1

if __name__ == "__main__":
    main()