import cv2
import numpy as np

from Building import Building, isNorthOf, isSouthOf, isEastOf, isWestOf, isNearTo, isIn
import Constants
from Description import Description
from Point import Point

# set up global variables for interactive map
gMapArr = None
gVillage = None
gClickCount = 0

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

'''
Loops through all points on the map and sees if they're described by a comparative description
then displays them on a map.
For utility - to see if DIRECTION_DIST_MAGIC_NUM is too small
'''
def displayUndescribedPoints(village):
    undescribedPoints = []
    for x in range(Constants.WIDTH):
        for y in range(Constants.HEIGHT):
            point = Point(x, y)
            dummyBuilding = Building("dummyBuilding", -1, [point])
            if all([len(elem) == 0 for elem in __getComparativePosition__(village, dummyBuilding)]):
                undescribedPoints.append(point)
    print(f'Num of undescribed points: {len(undescribedPoints)}')
    mapArr = __createEmptyMap__()
    for building in village.getBuildings():
        __replacePoints__(mapArr, building.getPoints(), Constants.WHITE)
    __replacePoints__(mapArr, undescribedPoints, Constants.RED)
    __display__(mapArr)

'''
Finds and displays the cluster of similar points fitting some comparison measure
'''
def displaySimilarPointCluster(village, comparison):
    descriptionMap = {}
    most = ("", None)
    for x in range(Constants.WIDTH):
        for y in range(Constants.HEIGHT):
            point = Point(x, y)
            description = __describeComparativePosition__(__getComparativePosition__(village, Building("dummyBuilding", -1, [point])))
            if description in descriptionMap.keys():
                descriptionMap[description].append(point)
            else:
                descriptionMap[description] = [point]
    for key, val in descriptionMap.items():
        if comparison(key, val, most[1]):
            most = (key, val)
    print(most[0])
    print(f'number of points: {len(most[1])}')
    mapArr = __createEmptyMap__()
    for building in village.getBuildings():
        __replacePoints__(mapArr, building.getPoints(), Constants.WHITE)
    __replacePoints__(mapArr, most[1], Constants.RED)
    __display__(mapArr)

'''
Displays an interactive map
First click outputs a comparative description and colors on the map all points that fit that description in teal
Second click does the same and colors the points red
Third click does the same as first click
Fourth click does the same as second click
And so on
'''
def displayInteractiveMap(village):
    global gVillage
    global gMapArr
    gVillage = village
    gMapArr = __setUpGMap__()
    # Set up mouse callback to react to click events
    cv2.namedWindow("Campus Map")
    cv2.setMouseCallback("Campus Map", __clickEvent__)
    __display__(gMapArr)

def __createEmptyMap__():
    return np.zeros((Constants.HEIGHT, Constants.WIDTH, 3))

def __replacePoints__(mapArr, points, val):
    for point in points:
        mapArr[point.y][point.x] = val

def __display__(mapArr):
    cv2.imshow("Campus Map", mapArr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def __clickEvent__(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global gClickCount
        global gMapArr
        isEvenClick = gClickCount % 2 == 0
        gClickCount = gClickCount + 1
        if isEvenClick:
            gMapArr = __setUpGMap__()
        clickBuilding = Building("clickBuilding", -1, [Point(x, y)])
        print(__describeComparativePosition__(__getComparativePosition__(gVillage, clickBuilding)))
        comparativelySimilarPoints = __getComparativelySimilarPoints__(gVillage, clickBuilding)
        __replacePoints__(gMapArr, comparativelySimilarPoints, Constants.TEAL if isEvenClick else Constants.RED)
        cv2.imshow("Campus Map", gMapArr)

def __getComparativePosition__(village, building):
    return [village.singleBuildingRelativePositioning(building, isIn, False),
            village.singleBuildingRelativePositioning(building, isNearTo, False),
            village.singleBuildingRelativePositioning(building, isNorthOf),
            village.singleBuildingRelativePositioning(building, isSouthOf),
            village.singleBuildingRelativePositioning(building, isEastOf),
            village.singleBuildingRelativePositioning(building, isWestOf)]

'''
Use breadth-first search starting from the initial x-y to find all points with the
same description based on direction
'''
def __getComparativelySimilarPoints__(village, building):
    description = __getComparativePosition__(village, building)
    center = building.getCenterForDisplay()
    checkedPoints = set([center])
    pointsToCheck = center.adjacentPoints()
    pointsToCheckSet = set(pointsToCheck)
    resultingPoints = [center]
    while len(pointsToCheck) > 0:
        otherPoint = pointsToCheck.pop(0)
        pointsToCheckSet.remove(otherPoint)
        checkedPoints.add(otherPoint)
        otherDescription = __getComparativePosition__(village, Building("nearClickBuilding", -2, [otherPoint]))
        sameDescription = True
        for i in range(5):
            if description[i] != otherDescription[i]:
                sameDescription = False
        if sameDescription:
            resultingPoints.append(otherPoint)
            for newPoint in otherPoint.adjacentPoints():
                if newPoint not in checkedPoints and newPoint not in pointsToCheckSet:
                    pointsToCheck.append(newPoint)
                    pointsToCheckSet.add(newPoint)
    return resultingPoints

def __describeComparativePosition__(description):
    descrip = Description()
    if len(description[0]) > 0:
        descrip.insideOf(description[0])
    if len(description[1]) > 0:
        descrip.nearTo(description[1])
    if len(description[2]) > 0:
        descrip.northOf(description[2])
    if len(description[3]) > 0:
        descrip.southOf(description[3])
    if len(description[4]) > 0:
        descrip.eastOf(description[4])
    if len(description[5]) > 0:
        descrip.westOf(description[5])
    return repr(descrip)

def __setUpGMap__():
    mapArr = __createEmptyMap__()
    for building in gVillage.getBuildings():
        __replacePoints__(mapArr, building.getPoints(), Constants.WHITE)
    return mapArr
