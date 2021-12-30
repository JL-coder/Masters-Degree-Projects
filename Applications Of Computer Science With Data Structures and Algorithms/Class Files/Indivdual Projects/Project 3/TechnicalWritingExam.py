#Import the parent class
from ITExamSuperClass import ITExamSuperClass

#Child class to the ITExamSuperClass. Class maintains the functions of the technical writing exam object.
class TechnicalWritingExam(ITExamSuperClass):
    #Class variables used to calculate grades
    MAX_SCORE = 100
    GRAMMER_PERCENT = 0.3
    SENTENCE_PERCENT = 0.3
    CONTENT_PERCENT = 0.4

    #Constructor for the technical writing exam class. Takes in 3 pieces of information from the technical writing exam:
    #grammer score, sentence score, and content score. Defaults to zero.
    def __init__(self, grammer = 0, sentence = 0, content = 0):
        super(TechnicalWritingExam, self).__init__()
        self.__grammerscore = grammer
        self.__sentencescore = sentence
        self.__contentscore = content

    # Setter method for the class. Checks that the score for the grammer part of the exam that is being set is
    # greater than 0 and less than or equal to 100. Returns true if it is and sets the score of the object, false if not.
    def setGrammerScore(self, score):
        if 0 <= score <= TechnicalWritingExam.MAX_SCORE:
            self.__grammerscore = score
            return True
        else:
            return False

    # Getter method for class. Returns the grammer score of the object.
    def getGrammerScore(self):
        return self.__grammerscore

    # Setter method for the class. Checks that the score for the sentence structure part of the exam that is being set is
    # greater than 0 and less than or equal to 100. Returns true if it is and sets the score of the object, false if not.
    def setSentenceStructureScore(self, score):
        if 0 <= score <= TechnicalWritingExam.MAX_SCORE:
            self.__sentencescore = score
            return True
        else:
            return False

    # Getter method for class. Returns the grammer score of the object.
    def getSentenceStructureScore(self):
        return self.__sentencescore

    # Setter method for the class. Checks that the score for the content part of the exam that is being set is
    # greater than 0 and less than or equal to 100. Returns true if it is and sets the score of the object, false if not.
    def setContentScore(self, score):
        if 0 <= score <= TechnicalWritingExam.MAX_SCORE:
            self.__contentscore = score
            return True
        else:
            return False

    # Getter method for class. Returns the content score of the object.
    def getContentScore(self):
        return self.__contentscore

    # Getter method for the class. Calculates the score for the technical writing exam using the constant variables. Returns
    # a letter grade based on the generated score using normal grade scale i.e greater or equal to a 90 is an A, 80 is a
    # B, etc. Score calculated - (grammer score * 0.3) + (sentence score * 0.3) + (content score * 0.4)
    def getExamGrade(self):
        score = ((self.getGrammerScore() * TechnicalWritingExam.GRAMMER_PERCENT) + (self.getSentenceStructureScore() *
                TechnicalWritingExam.SENTENCE_PERCENT) + (self.getContentScore() * TechnicalWritingExam.CONTENT_PERCENT))
        self.setExamScore(score)
        return super().getExamGrade()

    # To string method for the class. Returns a string version of the exam title and score.
    def toString(self):
        return super().toString()