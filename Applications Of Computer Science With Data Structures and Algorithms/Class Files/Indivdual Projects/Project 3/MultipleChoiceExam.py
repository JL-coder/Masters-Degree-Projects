#Import the parent class
from ITExamSuperClass import ITExamSuperClass

#Child class to the ITExamSuperClass. Class maintains the functions of the multiple choice exam object.
class MultipleChoiceExam(ITExamSuperClass):
    #Class Variable used to calculate grade
    POINTS_PER_QUESTION = 2

    # Constructor for the multiple choice exam class. Takes in 2 pieces of information from the multiple choice exam:
    # the total number of questions and the number of questions correctly answered. Defaults to zero.
    def __init__(self, num_questions = 0, correct_num_questions = 0):
        super(MultipleChoiceExam, self).__init__()
        self.__numquestions = num_questions
        self.__correctnumquestions = correct_num_questions

    # Setter method for the class. Checks that the total number of questions for the exam is greater than 0.
    # Returns true if it is and sets the total number of questions for the object, false if not.
    def setTotalNumOfMCQuestion(self, total_num):
        if total_num > 0:
            self.__numquestions = total_num
            return True
        else:
            return False

    #Getter method for the class. Returns the total number of multiple choice questions.
    def getTotalNumOfMCQuestion(self):
        return self.__numquestions

    # Setter method for the class. Checks that the correct number of questions for the exam is greater than 0 and less
    # than the total number of questions. Returns true if it is and sets the correct number of questions for the object,
    # false if not.
    def setCorrectNumOfMCQuestion(self, correct_num, total_num):
        if correct_num >= 0 and correct_num <= total_num:
            self.__correctnumquestions = correct_num
            return True
        else:
            return False

    # Getter method for the class. Returns the correct number of multiple choice questions.
    def getCorrectNumOfMCQuestion(self):
        return self.__correctnumquestions

    # Getter method for the class. Calculates the score for the multiple choice exam using the constant variables. Returns
    # a letter grade based on the generated score using normal grade scale i.e greater or equal to a 90 is an A, 80 is a
    # B, etc. Score calculated - ((correct mmultiple choice questions * 2) / (total number of questions * 2)) * 100
    def getExamGrade(self):
        score = ((self.getCorrectNumOfMCQuestion() * MultipleChoiceExam.POINTS_PER_QUESTION) /
                 (self.getTotalNumOfMCQuestion() * MultipleChoiceExam.POINTS_PER_QUESTION)) * ITExamSuperClass.MAX_SCORE
        self.setExamScore(score)
        return super().getExamGrade()

    # To string method for the class. Returns a string version of the exam title and score.
    def toString(self):
        return super().toString()
