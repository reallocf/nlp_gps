import math

import Constants
from Description import Description
from Location import Location
from Point import Point
import Utils

class Building():
    def __init__(self, name, buildingId, points):
        self.name = name
        self.id = buildingId
        self.points = set(points)
        self.area = len(self.points)
        self.boundingBoxTopLeft, self.boundingBoxBottomRight, self.boundingBoxPoints = self.__calcBoundingBox__(points)
        self.center = self.__calcCenter__(self.boundingBoxTopLeft, self.boundingBoxBottomRight)
        self.isRectangular, self.isDoubleSymmetricNotRectangular, self.isOnlyLeftRightSymmetric, self.isOnlyTopBottomSymmetric, self.isNotSymmetric = self.__calcSimilarity__(self.points, self.boundingBoxPoints, self.center)
        assert(Utils.exactlyOneOf([self.isRectangular, self.isDoubleSymmetricNotRectangular, self.isOnlyLeftRightSymmetric, self.isOnlyTopBottomSymmetric, self.isNotSymmetric]))
        self.isLongerLeftRight = self.__calcIsLongerLeftRight__(self.boundingBoxTopLeft, self.boundingBoxBottomRight)
        self.isLongerTopBottom = self.__calcIsLongerTopBottom__(self.boundingBoxTopLeft, self.boundingBoxBottomRight)
        self.isLengthSame = self.__calcIsLengthSame__(self.boundingBoxTopLeft, self.boundingBoxBottomRight)
        assert(Utils.exactlyOneOf([self.isLongerLeftRight, self.isLongerTopBottom, self.isLengthSame]))
        self.numberOfTouchingBoundingBoxCorners = self.__calcNumberOfTouchingBoundingBoxCorners__(self.boundingBoxTopLeft, self.boundingBoxBottomRight, self.points)
        self.isSkinny = self.__calcIsSkinny__(self.boundingBoxTopLeft, self.boundingBoxBottomRight)
        self.isSmall, self.isMedium, self.isLarge = self.__calcSize__(self.area)        
        assert(Utils.exactlyOneOf([self.isSmall, self.isMedium, self.isLarge]))
        self.shape = self.__describeShape__()
        self.location = self.__calcLocation__(self.center)

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

    def describeBuildingWithShape(self):
        return [self.name,
                self.center,
                self.area,
                self.boundingBoxTopLeft,
                self.boundingBoxBottomRight,
                self.shape]

    def describeBuildingWithShapeAndLocation(self):
        return [self.name,
                self.center,
                self.area,
                self.boundingBoxTopLeft,
                self.boundingBoxBottomRight,
                self.shape,
                self.location]

    '''
    Uniquely describes each building on Columbia map based solely on shape described in natural language.
    Not all descriptors are needed to uniquely describe each building, follows this tree structure to determine descriptors.

    rectangular
        longer left-right than top-bottom
            small
            medium
            large
        longer top-bottom than left-right
            is skinny
                small
                medium
                large
            is not skinny
                small
                medium
                large
        same left-right and top-bottom
    double symmetric but not rectangular
        longer left-right than top-bottom
            touches on 4 bounding box corners
            touches on 3 bounding box corners
            touches on 2 bounding box corners
            touches on 1 bounding box corner
            touches on no bounding box corners
                small
                medium
                large
        longer top-bottom than left-right
        same left-right and top-bottom
    only left-right symmetric
        longer left-right than top-bottom
        longer top-bottom than left-right
        same left-right and top-bottom
    only top-bottom symmetric
        longer left-right than top-bottom
        longer top-bottom than left-right
        same left-right and top-bottom
    not symmetric
        longer left-right than top-bottom
            touches on 4 bounding box corners
            touches on 3 bounding box corners
            touches on 2 bounding box corners
            touches on 1 bounding box corner
                is skinny
                is not skinny
            touches on no bounding box corners
        longer top-bottom than left-right
        same left-right and top-bottom
    '''
    def __describeShape__(self):
        description = Description()
        if self.isRectangular:
            description.isRectangular()
            if self.isLongerLeftRight:
                description.isLongerLeftRight()
                if self.isSmall:
                    description.isSmall()
                elif self.isMedium:
                    description.isMedium()
                else:
                    description.isLarge()
            elif self.isLongerTopBottom:
                description.isLongerTopBottom()
                if self.isSkinny:
                    description.isSkinny()
                    if self.isSmall:
                        description.isSmall()
                    elif self.isMedium:
                        description.isMedium()
                    else:
                        description.isLarge()
                else:
                    description.isNotSkinny()
                    if self.isSmall:
                        description.isSmall()
                    elif self.isMedium:
                        description.isMedium()
                    else:
                        description.isLarge()
            else:
                description.isLengthSameLeftRightTopBottom()
        elif self.isDoubleSymmetricNotRectangular:
            description.isDoubleSymmetricNotRectangular()
            if self.isLongerLeftRight:
                description.isLongerLeftRight()
                description.touchesOnXBoundingBoxCorners(self.numberOfTouchingBoundingBoxCorners)
                if (self.numberOfTouchingBoundingBoxCorners == 0):
                    if self.isSkinny:
                        description.isSkinny()
                    else:
                        description.isNotSkinny()
            elif self.isLongerTopBottom:
                description.isLongerTopBottom()
            else:
                description.isLengthSameLeftRightTopBottom()
        elif self.isOnlyLeftRightSymmetric:
            description.isOnlyLeftRightSymmetric()
            if self.isLongerLeftRight:
                description.isLongerLeftRight()
            elif self.isLongerTopBottom:
                description.isLongerTopBottom()
            else:
                description.isLengthSameLeftRightTopBottom()
        elif self.isOnlyTopBottomSymmetric:
            description.isOnlyTopBottomSymmetric()
            if self.isLongerLeftRight:
                description.isLongerLeftRight()
            elif self.isLongerTopBottom:
                description.isLongerTopBottom()
            else:
                description.isLengthSameLeftRightTopBottom()
        else:
            description.isNotSymmetric()
            if self.isLongerLeftRight:
                description.isLongerLeftRight()
                description.touchesOnXBoundingBoxCorners(self.numberOfTouchingBoundingBoxCorners)
                if (self.numberOfTouchingBoundingBoxCorners == 1):
                    if self.isSmall:
                        description.isSmall()
                    elif self.isMedium:
                        description.isMedium()
                    else:
                        description.isLarge()
            elif self.isLongerTopBottom:
                description.isLongerTopBottom()
            else:
                description.isLengthSameLeftRightTopBottom()        
        return description

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

    def __calcSimilarity__(self, points, boundingBoxPoints, center):
        isRectangular = self.__calcIsRectangular__(points, boundingBoxPoints)
        isLeftRightSymmetric = self.__calcIsLeftRightSymmetric__(points, center)
        isTopBottomSymmetric = self.__calcIsTopBottomSymmetric__(points, center)
        return (isRectangular,
            not isRectangular and isLeftRightSymmetric and isTopBottomSymmetric,
            not isRectangular and isLeftRightSymmetric and not isTopBottomSymmetric,
            not isRectangular and not isLeftRightSymmetric and isTopBottomSymmetric,
            not isRectangular and not isLeftRightSymmetric and not isTopBottomSymmetric)

    def __calcIsRectangular__(self, points, boundingBoxPoints):
        return all(boundingBoxPoint in points for boundingBoxPoint in boundingBoxPoints)

    def __calcIsLeftRightSymmetric__(self, points, center):
        return len([point for point in points if point.relativePoint((center.x - point.x) * 2, 0) not in points]) < Constants.SIMILARITY_MAGIC_NUM

    def __calcIsTopBottomSymmetric__(self, points, center):
        return len([point for point in points if point.relativePoint(0, (center.y - point.y) * 2) not in points]) < Constants.SIMILARITY_MAGIC_NUM

    def __calcIsLongerLeftRight__(self, topLeft, bottomRight):
        return (bottomRight.x - topLeft.x) - (bottomRight.y - topLeft.y) > Constants.RELATIVE_LENGTH_MAGIC_NUM

    def __calcIsLongerTopBottom__(self, topLeft, bottomRight):
        return (bottomRight.y - topLeft.y) - (bottomRight.x - topLeft.x) > Constants.RELATIVE_LENGTH_MAGIC_NUM

    def __calcIsLengthSame__(self, topLeft, bottomRight):
        return -Constants.RELATIVE_LENGTH_MAGIC_NUM <= (bottomRight.x - topLeft.x) - (bottomRight.y - topLeft.y) <= Constants.RELATIVE_LENGTH_MAGIC_NUM

    def __calcNumberOfTouchingBoundingBoxCorners__(self, topLeft, bottomRight, points):
        return sum([1 if topLeft in points else 0, 1 if bottomRight in points else 0, 1 if Point(topLeft.x, bottomRight.y) in points else 0, 1 if Point(bottomRight.x, topLeft.y) in points else 0])

    def __calcIsSkinny__(self, topLeft, bottomRight):
        return abs((bottomRight.x - topLeft.x) - (bottomRight.y - topLeft.y)) > Constants.SKINNINESS_MAGIC_NUM

    def __calcSize__(self, numberOfPoints):
        if numberOfPoints <= Constants.SMALL_MED_DIVIDE_MAGIC_NUM:
            return True, False, False
        elif numberOfPoints <= Constants.MED_LARGE_DIVIDE_MAGIC_NUM:
            return False, True, False
        else:
            return False, False, True

    def __calcLocation__(self, center):
        return Location(center)

def isRectangular(building):
    return building.isRectangular

def isDoubleSymmetricNotRectangular(building):
    return building.isDoubleSymmetricNotRectangular

def isOnlyLeftRightSymmetric(building):
    return building.isLeftRightSymmetric

def isOnlyTopBottomSymmetric(building):
    return building.isTopBottomSymmetric

def isNotSymmetric(building):
    return building.isNotSymmetric

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

def isSkinny(building):
    return building.isSkinny

def isNotSkinny(building):
    return not building.isSkinny

def isSmall(building):
    return building.isSmall

def isMedium(building):
    return building.isMedium

def isLarge(building):
    return building.isLarge