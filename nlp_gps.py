import cv2
import numpy as np

import Building
import Constants
from Description import Description
import MapViewer
from Point import Point
from Village import Village
import Utils

def main():
    buildingTable = read_in_table_data()
    columbia = Village(Constants.MAP_NAME, buildingTable)
    MapViewer.displayMapWithVillage(
        columbia,
        highlightByCondition=[
            (Building.isRectangular, Constants.RED),
            (Building.isDoubleSymmetricNotRectangular, Constants.YELLOW),
            (Building.isOnlyLeftRightSymmetric, Constants.BLUE),
            (Building.isOnlyTopBottomSymmetric, Constants.GREEN),
            (Building.isNotSymmetric, Constants.PURPLE)
        ]
    )
    MapViewer.displayMapWithVillage(
        columbia,
        highlightByCondition=[
            (Building.isLongerLeftRight, Constants.RED),
            (Building.isLongerTopBottom, Constants.BLUE),
            (Building.isLengthSame, Constants.GREEN)
        ]
    )
    MapViewer.displayMapWithVillage(
        columbia,
        highlightByCondition=[
            (Building.noTouchingBoundingBoxPoints, Constants.PURPLE),
            (Building.oneTouchingBoundingBoxPoint, Constants.YELLOW),
            (Building.twoTouchingBoundingBoxPoints, Constants.RED),
            (Building.threeTouchingBoundingBoxPoints, Constants.GREEN),
            (Building.fourTouchingBoundingBoxPoints, Constants.BLUE)
        ]
    )
    MapViewer.displayMapWithVillage(
        columbia,
        highlightByCondition=[
            (Building.isSkinny, Constants.RED),
            (Building.isNotSkinny, Constants.BLUE)
        ]
    )
    MapViewer.displayMapWithVillage(
        columbia,
        highlightByCondition=[
            (Building.isSmall, Constants.RED),
            (Building.isMedium, Constants.BLUE),
            (Building.isLarge, Constants.GREEN)
        ]
    )
    printBuildingDescriptionsByShape(columbia)
    printBuildingDescriptionsByShapeAndLocation(columbia)
    printBuildingsNearby(columbia)
    printBuildingsByDirectionalPositions(columbia)
    MapViewer.displayInteractiveMap(columbia)
    MapViewer.displaySimilarPointCluster(columbia, Utils.largest)
    MapViewer.displaySimilarPointCluster(columbia, Utils.smallest)
    MapViewer.displaySimilarPointCluster(columbia, Utils.largestNotInBuilding)

def read_in_table_data():
    with open(Constants.TABLE_NAME) as f:
        return {int(splitLine[0]) : splitLine[1] for splitLine in [line.split() for line in f.readlines()]}

def printBuildingDescriptionsByShape(village):
    buildingDescriptions = village.describeBuildingsByShape()
    print("\n".join([str(description) for description in buildingDescriptions]))

def printBuildingDescriptionsByShapeAndLocation(village):
    buildingDescriptions = village.describeBuildingsByShapeAndLocation()
    print("\n".join([str(description) for description in buildingDescriptions]))

def printBuildingsNearby(village):
    for building in village.getBuildings():
        for otherBuilding in village.getBuildings():
            if building.isNear(otherBuilding):
                print(f'{building.name}: {otherBuilding.name}')

def printBuildingsByDirectionalPositions(village):
    northMatrix = village.describeBuildingsByRelativePositioning(Building.isNorthOf)
    southMatrix = village.describeBuildingsByRelativePositioning(Building.isSouthOf)
    eastMatrix = village.describeBuildingsByRelativePositioning(Building.isEastOf)
    westMatrix = village.describeBuildingsByRelativePositioning(Building.isWestOf)
    for building in village.getBuildings():
        description = Description()
        if len(northMatrix[building]) > 0:
            description.northOf(northMatrix[building])
        if len(southMatrix[building]) > 0:
            description.southOf(southMatrix[building])
        if len(eastMatrix[building]) > 0:
            description.eastOf(eastMatrix[building])
        if len(westMatrix[building]) > 0:
            description.westOf(westMatrix[building])
        print(f'{building.name} {description}')

if __name__ == "__main__":
    main()
