import cv2
import numpy as np

import Building
import Constants
import MapViewer
from Point import Point
from Village import Village

def read_in_table_data():
    with open(Constants.TABLE_NAME) as f:
        return {int(splitLine[0]) : splitLine[1] for splitLine in [line.split() for line in f.readlines()]}

def printBuildingDescriptionsOnlyShape(village):
    buildingDescriptions = village.describeBuildingsByShape()
    print("\n".join([str(description) for description in buildingDescriptions]))

if __name__ == "__main__":
    buildingTable = read_in_table_data()
    columbia = Village(Constants.MAP_NAME, buildingTable)
    printBuildingDescriptionsOnlyShape(columbia)
    # MapViewer.displayMapWithVillage(
    #     columbia,
    #     highlightByCondition=[
    #         (Building.isRectangular, Constants.RED),
    #         (Building.isDoubleSymmetricNotRectangular, Constants.YELLOW),
    #         (Building.isOnlyLeftRightSymmetric, Constants.BLUE),
    #         (Building.isOnlyTopBottomSymmetric, Constants.GREEN),
    #         (Building.isNotSymmetric, Constants.PURPLE)
    #     ]
    # )
    # MapViewer.displayMapWithVillage(
    #     columbia,
    #     highlightByCondition=[
    #         (Building.isLongerLeftRight, Constants.RED),
    #         (Building.isLongerTopBottom, Constants.BLUE),
    #         (Building.isLengthSame, Constants.GREEN)
    #     ]
    # )
    # MapViewer.displayMapWithVillage(
    #     columbia,
    #     highlightByCondition=[
    #         (Building.noTouchingBoundingBoxPoints, Constants.PURPLE),
    #         (Building.oneTouchingBoundingBoxPoint, Constants.YELLOW),
    #         (Building.twoTouchingBoundingBoxPoints, Constants.RED),
    #         (Building.threeTouchingBoundingBoxPoints, Constants.GREEN),
    #         (Building.fourTouchingBoundingBoxPoints, Constants.BLUE)
    #     ]
    # )
    # MapViewer.displayMapWithVillage(
    #     columbia,
    #     highlightByCondition=[
    #         (Building.isSkinny, Constants.RED),
    #         (Building.isNotSkinny, Constants.BLUE)
    #     ]
    # )
    # MapViewer.displayMapWithVillage(
    #     columbia,
    #     highlightByCondition=[
    #         (Building.isSmall, Constants.RED),
    #         (Building.isMedium, Constants.BLUE),
    #         (Building.isLarge, Constants.GREEN)
    #     ]
    # )
