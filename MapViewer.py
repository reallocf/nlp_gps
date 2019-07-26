import cv2
import numpy as np

from Building import Building
import Constants

def displayMapWithBuildings(buildingList):
    mapArr = __createEmptyMap__()
    for building in buildingList:
        __replacePoints__(mapArr, building.getPoints(), Constants.WHITE)
    __display__(mapArr)

def __createEmptyMap__():
    return np.zeros((Constants.HEIGHT, Constants.WIDTH))

def __replacePoints__(mapArr, points, val):
    for point in points:
        mapArr[point.y][point.x] = val

def __display__(mapArr):
    cv2.imshow("Campus Map", mapArr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
