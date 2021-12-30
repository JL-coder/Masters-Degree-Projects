
#Parent class. Used to manage the title and exam score of the class.
class ITExamSuperClass:
    #Class variable used to calculate exam scores
    MAX_SCORE = 100

    #Constructor for the class. Takes in a title and score. Each defaults to zero if no other entry.
    def __init__(self, title = "None", score = 0):
        self.__examtitle = title
        self.__examscore = score

    # Setter method for the class. Checks that the title length for the exam is greater than 0.
    # Returns true if it is and sets the title for the object, false if not.
    def setExamTitle(self, title):
        if len(title) > 0:
            self.__examtitle = title
            return True
        else:
            return False

    # Getter method for the class. Returns the title of the exam.
    def getExamTitle(self):
        return self.__examtitle

    #Setter method for the class. Checks that the score being set is greater than or equal to zero and less than or equal
    # to 100.
    def setExamScore(self, score):
        if 0 <= score <= ITExamSuperClass.MAX_SCORE:
            self.__examscore = score
            return True
        else:
            return False

    # Getter method for the class. Returns the score of the exam.
    def getExamScore(self):
        return self.__examscore

    # Getter method for the class. Returns a letter grade score using normal grade scale i.e greater or equal to a 90 is
    # an A, 80 is a B, etc.
    def getExamGrade(self):
        if self.getExamScore() >= 90:
            return "A"
        elif self.getExamScore() >= 80:
            return "B"
        elif self.getExamScore() >= 70:
            return "C"
        elif self.getExamScore() >= 60:
            return "D"
        else:
            return "F"

    # To string method for the class. Returns a string version of the exam title and score.
    def toString(self):
        s = "\nExam Title: " + self.getExamTitle()
        s += "\nExam Score: " + str(self.getExamScore())
        return s
