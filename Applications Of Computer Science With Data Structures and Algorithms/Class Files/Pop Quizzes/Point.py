class Point:

    def __init__(self, xcord=0, ycord=0):
        self.__xcoordinate = xcord
        self.__ycoordinate = ycord

    def getXCoordinates(self):
        return self.__xcoordinate

    def setXCoordinates(self, xcord):
        self.__xcoordinate = xcord
        return self.__xcoordinate
    def increaseOneOnX(self):
        new_x = self.getXCoordinates() + 1
        self.__xcoordinate = new_x
        return self.__xcoordinate

    def getYCoordinates(self):
        return self.__ycoordinate

    def setYCoordinates(self, ycord):
        self.__ycoordinate = ycord
        return self.__ycoordinate

    def increaseOneOnY(self):
        new_y = self.getYCoordinates() + 1
        self.__ycoordinate = new_y
        return self.__ycoordinate

    def toString(self):
        #s = "\nX Coordinate: " + str(self.getXCoordinates())
        #s += "\nY Coordinate:  " + str(self.getYCoordinates())
        s = "\nThe coordinate of the point is (" + str(self.getXCoordinates()) + ", " + str(self.getYCoordinates()) + ")"
        return s