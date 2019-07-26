import Constants
from Point import Point

class Building():
    def __init__(self, points):
        self.points = points
        self.boundingBoxTopLeft, self.boundingBoxBottomRight, self.boundingBoxPoints = self.__getBoundingBox__(points)

    def __getBoundingBox__(self, points):
        top = Constants.HEIGHT + 1
        left = Constants.WIDTH + 1
        bottom = -1
        right = -1
        for point in points:
            if point.y < top:
                top = point.y
            if point.y > bottom:
                bottom = point.y
            if point.x < left:
                left = point.x
            if point.x > right:
                right = point.x
        assert(top < bottom)
        assert(left < right)
        boundingBoxPoints = []
        for y in range(top, bottom):
            boundingBoxPoints.append(Point(left, y))
            boundingBoxPoints.append(Point(right, y))
        for x in range(left, right):
            boundingBoxPoints.append(Point(x, top))
            boundingBoxPoints.append(Point(x, bottom))
        return (top, left), (bottom, right), boundingBoxPoints
    
    def getSize(self):
        return len(self.points)

    def getPoints(self):
        return self.points
