#Import the parent class
from ITExamSuperClass import ITExamSuperClass

#Child class to the ITExamSuperClass. Class maintains the functions of the analytical programming exam object.
class AnalyticalProgrammingExam(ITExamSuperClass):
    # Class variables used to calculate grades
    MAX_SCORE = 100
    SHORT_ANSWER_PERCENT = 0.3
    PROGRAMMING_PERCENT = 0.7

    #Constructor for the analytical programming exam class. Takes in 2 pieces of information from the analytical exam,
    # the short answer and programming section. Defaults to zero.
    def __init__(self, short = 0, programming = 0):
        super(AnalyticalProgrammingExam, self).__init__()
        self.__shortanswerscore = short
        self.__programminganswerscore = programming

    #Setter method for the class. Checks that the score for the short answer part of the exam that is being set is
    # greater than 0 and less than or equal to 100. Returns true if it is and sets the score of the object, false if not.
    def setShortAnswerScore(self, score):
        if 0 <= score <= AnalyticalProgrammingExam.MAX_SCORE:
            self.__shortanswerscore = score
            return True
        else:
            return False

    #Getter method for class. Returns the short answer score of the object.
    def getShortAnswerScore(self):
        return self.__shortanswerscore

    # Setter method for the class. Checks that the score for the programming part of the exam that is being set is
    # greater than 0 and less than or equal to 100. Returns true if it is and sets the score of the object, false if not.
    def setProgrammingScore(self, score):
        if 0 <= score <= AnalyticalProgrammingExam.MAX_SCORE:
            self.__programminganswerscore = score
            return True
        else:
            return False

    #Getter method for class. Returns the programming score of the object.
    def getProgrammingScore(self):
        return self.__programminganswerscore

    #Getter method for the class. Calculates the score for the short answer exam using the constant variables. Returns
    # a letter grade based on the generated score using normal grade scale i.e greater or equal to a 90 is an A, 80 is a
    #B, etc. Score calculated - (short answer score * 0.3) + (programming score * 0.7).
    def getExamGrade(self):
        score = ((self.getShortAnswerScore() * AnalyticalProgrammingExam.SHORT_ANSWER_PERCENT) +
                 (self.getProgrammingScore() * AnalyticalProgrammingExam.PROGRAMMING_PERCENT))
        self.setExamScore(score)
        return super().getExamGrade()

    #To string method for the class. Returns a string version of the exam title and score.
    def toString(self):
        return super().toString()
