class Set:
    def __init__(self, elements): # Create a Set Using a List
        els = []
        for x in elements:
            if x not in els:
                els.append(x)
        self.__elements = els

    def getElements(self):
        return self.__elements

    def getSize(self):
        return len(self.__elements)

    def contains(self, element):
        return element in self.getElements()

    def add(self, element):
        self.getElements().append(element)

    def remove(self, element):
        self.getElements().remove(element)

    def isSubsetOf(self, setB):
        for element in self.getElements():
            if element not in setB.getElements():
                return False
        return True

    def equal(self, setB):
        if self.getSize() != setB.getSize():
            return False
        else:
            return self.isSubsetOf(setB) and setB.issubset(self)

    def union(self, setB):
        return Set(self.getElements() + setB.getElements())

    def intersect(self, setB):
        els = []
        for x in self.getElements():
            if x in setB.getElements():
                els.append(x)
        return Set(els)

    def subtract(self, setB):
        els = []
        for x in self.getElements():
            if x not in setB.getElements():
                els.append(x)
        return Set(els)

    def __str__(self):
        return "<Set: {0}>".format(self.getElements())