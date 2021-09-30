import math

class Point:
    X = 0
    Y = 0

    def __init__(self, x, y):
        self.X = x
        self.Y = y

class Line:
    def __init__(self):
        self.__PointA = Point(0, 0)
        self.__PointB = Point(1, 1)

    def getLength(self):
        return math.sqrt(math.pow(self.__PointA.X - self.__PointB.X, 2) + math.pow(self.__PointA.Y - self.__PointB.Y, 2))
    
line = Line()
print(line.getLength())