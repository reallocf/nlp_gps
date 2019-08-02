import math

import Constants
from Point import Point

class Building():
    def __init__(self, buildingId, points):
        self.id = buildingId
        self.points = set(points)
        self.boundingBoxTopLeft, self.boundingBoxBottomRight, self.boundingBoxPoints = self.__calcBoundingBox__(points)
        self.center = self.__calcCenter__(self.boundingBoxTopLeft, self.boundingBoxBottomRight)
        self.isRectangular = self.__calcIsRectangular__(self.points, self.boundingBoxPoints)
        self.isLeftRightSymmetric = self.__calcIsLeftRightSymmetric__(self.points, self.center)
        self.isTopBottomSymmetric = self.__calcIsTopBottomSymmetric__(self.points, self.center)
        self.isLongerLeftRight = self.__calcIsLongerLeftRight__(self.boundingBoxTopLeft, self.boundingBoxBottomRight)
        self.isLongerTopBottom = self.__calcIsLongerTopBottom__(self.boundingBoxTopLeft, self.boundingBoxBottomRight)
        self.isLengthSame = self.__calcIsLengthSame__(self.boundingBoxTopLeft, self.boundingBoxBottomRight)
        self.numberOfTouchingBoundingBoxCorners = self.__calcNumberOfTouchingBoundingBoxCorners__(self.boundingBoxTopLeft, self.boundingBoxBottomRight, self.points)

    def getId(self):
        return self.id

    def getSize(self):
        return len(self.points)

    def getPoints(self):
        return self.points

    def getBoundingBoxPoints(self):
        return self.boundingBoxPoints

    def getCenterForDisplay(self):
        return self.center.forDisplay()

    def __calcBoundingBox__(self, points):
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
        return Point(left, top), Point(right, bottom), boundingBoxPoints

    def __calcCenter__(self, topLeft, bottomRight):
        return Point((topLeft.x + bottomRight.x) / 2, (topLeft.y + bottomRight.y) / 2)

    def __calcIsRectangular__(self, points, boundingBoxPoints):
        return all(boundingBoxPoint in points for boundingBoxPoint in boundingBoxPoints)

    def __calcIsLeftRightSymmetric__(self, points, center):
        return len([point for point in points if point.relativePoint((center.x - point.x) * 2, 0) not in points]) < Constants.SIMILARITY_MAGIC_NUM

    def __calcIsTopBottomSymmetric__(self, points, center):
        return len([point for point in points if point.relativePoint(0, (center.y - point.y) * 2) not in points]) < Constants.SIMILARITY_MAGIC_NUM

    def __calcIsLongerLeftRight__(self, topLeft, bottomRight):
        return (bottomRight.x - topLeft.x) - (bottomRight.y - topLeft.y) > Constants.RELATIVE_LENGTH_MAGIC_NUM

    def __calcIsLongerTopBottom__(self, topLeft, bottomRight):
        return (bottomRight.y - topLeft.y) - (bottomRight.x - topLeft.x) > -Constants.RELATIVE_LENGTH_MAGIC_NUM

    def __calcIsLengthSame__(self, topLeft, bottomRight):
        return -Constants.RELATIVE_LENGTH_MAGIC_NUM <= (bottomRight.x - topLeft.x) - (bottomRight.y - topLeft.y) <= Constants.RELATIVE_LENGTH_MAGIC_NUM

    def __calcNumberOfTouchingBoundingBoxCorners__(self, topLeft, bottomRight, points):
        return sum([1 if topLeft in points else 0, 1 if bottomRight in points else 0, 1 if Point(topLeft.x, bottomRight.y) in points else 0, 1 if Point(bottomRight.x, topLeft.y) in points else 0])

def isRectangular(building):
    return building.isRectangular

def isLeftRightSymmetric(building):
    return building.isLeftRightSymmetric

def isTopBottomSymmetric(building):
    return building.isTopBottomSymmetric

def isDoubleSymmetric(building):
    return building.isLeftRightSymmetric and building.isTopBottomSymmetric

def isDoubleSymmetricNotRectangular(building):
    return not building.isRectangular and building.isLeftRightSymmetric and building.isTopBottomSymmetric

def isOnlyLeftRightSymmetric(building):
    return not building.isRectangular and building.isLeftRightSymmetric and not building.isTopBottomSymmetric

def isOnlyTopBottomSymmetric(building):
    return not building.isRectangular and not building.isLeftRightSymmetric and building.isTopBottomSymmetric

def isNotSymmetric(building):
    return not building.isRectangular and not building.isLeftRightSymmetric and not building.isTopBottomSymmetric

def isLongerLeftRight(building):
    return building.isLongerLeftRight

def isLongerTopBottom(building):
    return building.isLongerTopBottom

def isLengthSame(building):
    return building.isLengthSame

def noTouchingBoundingBoxPoints(building):
    return building.numberOfTouchingBoundingBoxCorners == 0

def oneTouchingBoundingBoxPoint(building):
    return building.numberOfTouchingBoundingBoxCorners == 1

def twoTouchingBoundingBoxPoints(building):
    return building.numberOfTouchingBoundingBoxCorners == 2

def threeTouchingBoundingBoxPoints(building):
    return building.numberOfTouchingBoundingBoxCorners == 3

def fourTouchingBoundingBoxPoints(building):
    return building.numberOfTouchingBoundingBoxCorners == 4
