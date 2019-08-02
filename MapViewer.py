import cv2
import numpy as np

from Building import Building
import Constants

def __alwaysFalse__(building):
        return False

def displayMapWithVillage(village, displayBoundingBoxes=(False, Constants.RED),
    displayCenterPoint=(False, Constants.GREEN), highlightByCondition=[(__alwaysFalse__, Constants.BLUE)]):
    mapArr = __createEmptyMap__()
    for building in village.getBuildings():
        __replacePoints__(mapArr, building.getPoints(), Constants.WHITE)
    for condition, color in highlightByCondition:
        for building in village.getBuildings():
            if condition(building):
                __replacePoints__(mapArr, building.getPoints(), color)
    if (displayBoundingBoxes[0]):
        for building in village.getBuildings():
            __replacePoints__(mapArr, building.getBoundingBoxPoints(), Constants.RED)
    if (displayCenterPoint[0]):
        for building in village.getBuildings():
            __replacePoints__(mapArr, building.getCenterForDisplay().allNearbyPoints(), Constants.GREEN)
    __display__(mapArr)

def __createEmptyMap__():
    return np.zeros((Constants.HEIGHT, Constants.WIDTH, 3))

def __replacePoints__(mapArr, points, val):
    for point in points:
        mapArr[point.y][point.x] = val

def __display__(mapArr):
    cv2.imshow("Campus Map", mapArr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
