#Import all the class information
from ITExamSuperClass import ITExamSuperClass
from MultipleChoiceExam import MultipleChoiceExam
from TechnicalWritingExam import TechnicalWritingExam
from AnalyticalProgrammingExam import AnalyticalProgrammingExam

#Global list variable. Used in several methods.
allExamsList = []

def main():
    #Variables control the while loops used in inputting information.
    boolean_flag = True
    boolean_switch = True
    boolean_switch2 = True
    user_more_exams = "This will always run at least once"

    #Main while loop displays the exam type menu and asks the user what exam they would like to input. The user enters a
    # number code based on the exam type. If the userm inputs "no" then the loop is exited. If user enters a unlisted
    # number then a warning is given and the user can try again.
    while boolean_flag:
        if user_more_exams != "no":
            print("")
            print("IT Exam Type Menu: ")
            print("1) Multiple Choice")
            print("2) Technical Writing")
            print("3) Analytical Programming")
            user_examtype_input = int(input("Enter your choice: "))
            # If the user inputs 1 then it enters into the next set of while loops. In this loop the user enters the
            # the exam title and the appropriate exam object is created based on the previous exam type entry. If the
            # title is left blank a warning is given and the user has the option to enter the title again.
            if user_examtype_input == 1:
                while boolean_switch:
                    print("")
                    user_exam_title = str(input("Enter the Exam Title: "))
                    exam_object = MultipleChoiceExam()
                    #If the title length is greater than zero than this while loop is turned off and the exam object is
                    #passed to the fillITExam function.
                    if exam_object.setExamTitle(user_exam_title):
                        boolean_switch = False
                        boolean_switch2 = True
                        fillITExam(exam_object)
                    else:
                        print("Sorry! The exam title is not valid. Please enter it again.")
                #Second set of while loops run after the first. Asks the user if there are any more exam inputs. If
                #there are then the main loop is re-entered and the previous loop is turned back on. Otherwise all loops
                #are turned off and the displayResults function is run.
                while boolean_switch2:
                    print("")
                    user_more_exams = str(input("More IT Exams (Yes/No)? ")).casefold()
                    if user_more_exams != "no":
                        boolean_switch = True
                        boolean_switch2 = False
                    else:
                        boolean_switch = False
                        boolean_switch2 = False
                        boolean_flag = False
                        displayResults(allExamsList)
            # If the user inputs 2 then it enters into the next set of while loops. In this loop the user enters the
            # the exam title and the appropriate exam object is created based on the previous exam type entry. If the
            # title is left blank a warning is given and the user has the option to enter the title again.
            elif user_examtype_input == 2:
                while boolean_switch:
                    print("")
                    user_exam_title = str(input("Enter the Exam Title: "))
                    exam_object = TechnicalWritingExam()
                    # If the title length is greater than zero than this while loop is turned off and the exam object is
                    # passed to the fillITExam function.
                    if exam_object.setExamTitle(user_exam_title):
                        boolean_switch = False
                        boolean_switch2 = True
                        fillITExam(exam_object)
                    else:
                        print("Sorry! The exam title is not valid. Please enter it again.")
                # Second set of while loops run after the first. Asks the user if there are any more exam inputs. If
                # there are then the main loop is re-entered and the previous loop is turned back on. Otherwise all loops
                # are turned off and the displayResults function is run.
                while boolean_switch2:
                    print("")
                    user_more_exams = str(input("More IT Exams (Yes/No)? ")).casefold()
                    if user_more_exams != "no":
                        boolean_switch = True
                        boolean_switch2 = False
                    else:
                        boolean_switch = False
                        boolean_switch2 = False
                        boolean_flag = False
                        displayResults(allExamsList)
            # If the user inputs 3 then it enters into the next set of while loops. In this loop the user enters the
            # the exam title and the appropriate exam object is created based on the previous exam type entry. If the
            # title is left blank a warning is given and the user has the option to enter the title again.
            elif user_examtype_input == 3:
                while boolean_switch:
                    print("")
                    user_exam_title = str(input("Enter the Exam Title: "))
                    exam_object = AnalyticalProgrammingExam()
                    # If the title length is greater than zero than this while loop is turned off and the exam object is
                    # passed to the fillITExam function.
                    if exam_object.setExamTitle(user_exam_title):
                        boolean_switch = False
                        boolean_switch2 = True
                        fillITExam(exam_object)
                    else:
                        print("Sorry! The exam title is not valid. Please enter it again.")
                # Second set of while loops run after the first. Asks the user if there are any more exam inputs. If
                # there are then the main loop is re-entered and the previous loop is turned back on. Otherwise all loops
                # are turned off and the displayResults function is run.
                while boolean_switch2:
                    print("")
                    user_more_exams = str(input("More IT Exams (Yes/No)? ")).casefold()
                    if user_more_exams != "no":
                        boolean_switch = True
                        boolean_switch2 = False
                    else:
                        boolean_switch = False
                        boolean_switch2 = False
                        boolean_flag = False
                        displayResults(allExamsList)
            else:
                print("")
                print("Sorry! No such choice. Please enter it again.")

#Function takes in an exam type object with a name and a score. The function then processes this object based on the
#exam type that the user previously inputted adding the scores for that type of exam to the object. This object is
# returned as part of the allExamsList.
def fillITExam(oneExamObject):
    #Switches that turn on and off the while loops in the function.
    boolean_switch1 = True
    boolean_switch2 = True
    boolean_switch3 = True

    #Check instace of oneExamobject to see if it is of MultipleChoiceExam
    if isinstance(oneExamObject, MultipleChoiceExam):
        #In this loop the passed parameter is renamed (so that its easier to differentiate while reading the code). Then
        #the user is asked to enter the total number of multiple choice questions. If the total is less than zero the
        #user is given the option of re-entering the number. Otherwise the number is set as part of the object and the
        #loop is turned off.
        while boolean_switch1:
            mc_object = oneExamObject
            try:
                user_total_num_mc = int(input("Total Number of Multiple Choice's Questions: "))
                if mc_object.setTotalNumOfMCQuestion(user_total_num_mc):
                    mc_object.setTotalNumOfMCQuestion(user_total_num_mc)
                    boolean_switch1 = False
                else:
                    print("")
                    print("Sorry! The number is not valid. Please enter it again.")
            except (ValueError, UnboundLocalError):
                print("Please enter a number")
        #In this loop the user is asked to enter the total number of correct multiple choice questions. If the number
        # is greater than zero and less than the total number of multiple choice questions than the object is set with
        # that number. The loop is turned off and the exam score is calculated and set for the object. The object is
        # than added to the allExamsList.
        while boolean_switch2:
            try:
                user_correct_num_mc = int(input("Total Number of Correct Multiple Choice's Questions: "))
                if mc_object.setCorrectNumOfMCQuestion(user_correct_num_mc, user_total_num_mc):
                    mc_object.setCorrectNumOfMCQuestion(user_correct_num_mc, user_total_num_mc)
                    boolean_switch2 = False
                    mc_object.setExamScore(((mc_object.getCorrectNumOfMCQuestion() * MultipleChoiceExam.POINTS_PER_QUESTION) /
                    (mc_object.getTotalNumOfMCQuestion() * MultipleChoiceExam.POINTS_PER_QUESTION)) * ITExamSuperClass.MAX_SCORE)
                    allExamsList.append(mc_object)
                else:
                    print("")
                    print("Sorry! The number is not valid. Please enter it again.")
            except (ValueError, UnboundLocalError):
                print("Please enter a number")

    # Check instace of oneExamobject to see if it is of TechinicalWritingExam
    elif isinstance(oneExamObject, TechnicalWritingExam):
        #In this loop the passed parameter is renamed (so that its easier to differentiate while reading the code). Then
        # the user is asked to enter the grammer score. If the total is less than zero the
        # user is given the option of re-entering the number. Otherwise the number is set as part of the object and the
        # loop is turned off.
        while boolean_switch1:
            tw_object = oneExamObject
            try:
                user_grammer_score = float(input("Score of Grammer Portion: "))
                if tw_object.setGrammerScore(user_grammer_score):
                    tw_object.setGrammerScore(user_grammer_score)
                    boolean_switch1 = False
                else:
                    print("")
                    print("Sorry! The score is not valid. Please enter it again.")
            except (ValueError, UnboundLocalError):
                print("Please enter a number")
        #The user is asked to enter the sentence structure score. If the total is less than zero the
        # user is given the option of re-entering the number. Otherwise the number is set as part of the object and the
        # loop is turned off.
        while boolean_switch2:
            try:
                user_sentence_score = float(input("Score of Sentence Structure Portion: "))
                if tw_object.setSentenceStructureScore(user_sentence_score):
                    tw_object.setSentenceStructureScore(user_sentence_score)
                    boolean_switch2 = False
                else:
                    print("")
                    print("Sorry! The score is not valid. Please enter it again.")
            except (ValueError, UnboundLocalError):
                print("Please enter a number")

        # The user is asked to enter the sentence structure score. If the total is less than zero the
        # user is given the option of re-entering the number. Otherwise the number is set as part of the object and the
        # loop is turned off and the exam score is calculated and set for the object. The object is
        # than added to the allExamsList.
        while boolean_switch3:
            try:
                user_content_score = float(input("Score of Content Portion: "))
                if tw_object.setContentScore(user_content_score):
                    tw_object.setContentScore(user_content_score)
                    boolean_switch3 = False
                    tw_object.setExamScore((tw_object.getGrammerScore() * TechnicalWritingExam.GRAMMER_PERCENT) + (tw_object.getSentenceStructureScore()
                    * TechnicalWritingExam.SENTENCE_PERCENT) + (tw_object.getContentScore() * TechnicalWritingExam.CONTENT_PERCENT))
                    allExamsList.append(tw_object)
                else:
                    print("")
                    print("Sorry! The score is not valid. Please enter it again.")
            except (ValueError, UnboundLocalError):
                print("Please enter a number")
    #Third option - analytical programming was chosen
    else:
        #In this loop the passed parameter is renamed (so that its easier to differentiate while reading the code). Then
        # the user is asked to enter the short answer score. If the total is less than zero the
        # user is given the option of re-entering the number. Otherwise the number is set as part of the object and the
        # loop is turned off.
        while boolean_switch1:
            try:
                user_sa_score = float(input("Score of Short Answer Section: "))
                ap_object = oneExamObject
                if ap_object.setShortAnswerScore(user_sa_score):
                    ap_object.setShortAnswerScore(user_sa_score)
                    boolean_switch1 = False
                else:
                    print("")
                    print("Sorry! The score is not valid. Please enter it again.")
            except (ValueError, UnboundLocalError):
                print("Please enter a number")

        #The user is asked to enter the short answer score. If the total is less than zero the
        # user is given the option of re-entering the number. Otherwise the number is set as part of the object and the
        # loop is turned off and the exam score is calculated and set for the object. The object is
        # than added to the allExamsList.
        while boolean_switch2:
            try:
                user_p_score = float(input("Score of Programming Section: "))
                if ap_object.setProgrammingScore(user_p_score):
                    ap_object.setProgrammingScore(user_p_score)
                    boolean_switch2 = False
                    ap_object.setExamScore((ap_object.getShortAnswerScore() * AnalyticalProgrammingExam.SHORT_ANSWER_PERCENT) + (ap_object.getProgrammingScore() *
                    AnalyticalProgrammingExam.PROGRAMMING_PERCENT))
                    allExamsList.append(ap_object)
                else:
                    print("")
                    print("Sorry! The score is not valid. Please enter it again.")
            except (ValueError, UnboundLocalError):
                print("Please enter a number")

#This function prints the exam title, score inputs, total score, and average score for all the exams entered. It takes
#in a list of exam objects.
def displayResults(allExamsList):
    #Counter variable
    total_score = 0

    #For loop goes through the allExamsList parameter and uses the toString class method to print out the exam title
    #and score. Then depending on which exam it is looping through at that point. It will proceed to output the entered
    #information and the final exam letter grade. The exam score is added to the counter variable and is printed out
    #last along with the average exam score.
    for exam in allExamsList:
        print(exam.toString())
        if isinstance(exam, MultipleChoiceExam):
            print("Total Number of MC Questions: " + str(exam.getTotalNumOfMCQuestion()))
            print("Total Number of Correct MC Questions: " + str(exam.getCorrectNumOfMCQuestion()))
            print("Final Grade: " + str(exam.getExamGrade()))
            total_score += exam.getExamScore()
        elif isinstance(exam, TechnicalWritingExam):
            print("Score of Grammer Portion:  " + str(exam.getGrammerScore()))
            print("Score of Sentence Portion: " + str(exam.getSentenceStructureScore()))
            print("Score of Content Portion: " + str(exam.getContentScore()))
            print("Final Grade: " + str(exam.getExamGrade()))
            total_score += exam.getExamScore()
        else:
            print("Score of Short Answer Section: " + str(exam.getShortAnswerScore()))
            print("Score of Programming Section: " + str(exam.getProgrammingScore()))
            print("Final Grade: " + str(exam.getExamGrade()))
            total_score += exam.getExamScore()
    print("")
    print("Total Score of All Exams: " + str(total_score))
    print("Average Score of All Exams: " + str((total_score) / len(allExamsList)))
if __name__ == "__main__":
    main()