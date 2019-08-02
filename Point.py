import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'

    def __eq__(self, other):
        return self.x == self.x and self.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def forDisplay(self):
        return Point(math.floor(self.x), math.floor(self.y))

    def relativePoint(self, xDiff, yDiff):
        return Point(self.x + xDiff, self.y + yDiff)

    def allNearbyPoints(self):
        ret = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                ret.append(self.relativePoint(x, y))
        return ret
