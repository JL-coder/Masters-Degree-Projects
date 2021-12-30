from MapEntry import MapEntry

class Map:
    def __init__(self):
        self.__entryList = list()

    def getEntryList(self):
        return self.__entryList

    def getNumberOfEntries(self):
        return len(self.getEntryList())

    def __contains(self, key):
        ndx = self.__findPosition(key)
        return ndx is not None # Return True or False

    def __findPosition(self, key):
        if self.getNumberOfEntries() == 0:
            return None
        else:
            for i in range(self.getNumberOfEntries()):
                if self.getEntryList()[i].getKey() == key:
                    return i
            return None

    def add(self, key, value):
        if self.__contains(key):
            print("Such Key-Value Pair has existed.")
        else:
            entry = MapEntry(key, value)
            self.getEntryList().append(entry)

    def remove(self, key):
        if self.__contains(key):
            ndx = self.__findPosition(key)
            self.getEntryList().pop(ndx)
        else:
            print("No Such Key-Value Pair.")

    def valueOf(self, key):
        if self.__contains(key):
            ndx = self.__findPosition(key)
            return self.getEntryList()[ndx].getValue()
        else:
            return "No Such Key-Value Pair."


    def updateValue(self, key = None, value = None):
        flag = False
        if key is not None and value is not None:
            for i in range(self.getNumberOfEntries()):
                if self.getEntryList()[i].getKey() == key:
                    self.getEntryList()[i].setValue(value)
                    flag = True

            if flag is True:
                return "Value has been updated."
            else:
                return "No Update is Needed."

    def __str__(self):
        if self.getNumberOfEntries() == 0:
            return "Empty Dictionary"
        else:
            output = "{"
            for i in range(self.getNumberOfEntries()):
                if i <= self.getNumberOfEntries() - 2:
                    output += (self.getEntryList()[i].getKey() + " : " + str(self.getEntryList()[i].getValue()) + ", ")
                else:
                    output += (self.getEntryList()[i].getKey() + " : " + str(self.getEntryList()[i].getValue()))
            return output + "}"