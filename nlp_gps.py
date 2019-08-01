import cv2
import numpy as np

import Constants
import MapViewer
from Point import Point
from Village import Village

class TwoDimRep():
    def __init__(self, rawData):
        self.data = self.__buildData__(rawData)

    def __buildData__(self, rawData):
        assert(len(rawData) == Constants.WIDTH * Constants.HEIGHT)
        twoDimRep = []
        for y in range(Constants.HEIGHT):
            twoDimRep.append([int(elem) for elem in rawData[y * Constants.WIDTH : (y + 1) * Constants.WIDTH]])
        return twoDimRep

    def __repr__(self):
        return "\n".join([str(row) for row in self.data])

    def ___waitUntilPress___(self):
        k = cv2.waitKey(0) & 0xFF
        cv2.destroyAllWindows()

    def displayTwoDim(self):
        cv2.imshow("Campus Map", np.array(
            [[255 if elem > 0 else 0 for elem in row] for row in self.data],
            dtype=np.uint8))
        self.___waitUntilPress___()

    """
    buildingMap is a map: buildingId -> pos (26 = most, 1 = least)
    """
    def displayWithHighlightedBuildings(self, buildingMap):
        assert(len(buildingMap) == Constants.BUILDING_NUM)
        cv2.imshow("Highlighted Map", np.array(
            [[(0, 0, (255 / Constants.BUILDING_NUM) * buildingMap[elem]) if elem > 0 else (0, 0, 0) for elem in row] for row in self.data],
            dtype=np.uint8))
        self.___waitUntilPress___()
        

class BuildingsRep():
    def __init__(self, buildingIds, rawData):
        self.data = self.__buildData__(buildingIds, rawData)

    def __buildData__(self, buildingIds, rawData):
        assert(len(rawData) == Constants.WIDTH * Constants.HEIGHT)
        buildingPixelRep = {k : [] for k in buildingIds}
        for y in range(Constants.HEIGHT):
            for x in range(Constants.WIDTH):
                buildingId = rawData[y * Constants.WIDTH + x]
                assert(buildingId == 0 or buildingId in buildingIds)
                if (buildingId != 0):
                    buildingPixelRep[buildingId].append(Point(x, y))
        return {k: Building(v) for k, v in buildingPixelRep.items()}

    def __repr__(self):
        return str(self.data)

    def getBySize(self):
        return {k: building.getSize() for k, building in self.data.items()}

    """
    returns map: buildingId -> size (26 = largest, 1 = smallest)
    """
    def orderBySizeMap(self):
        i = 1
        ret = {}
        for k, _ in sorted(self.data.items(), key=lambda item: item[1].getSize()):
            ret[k] = i
            i = i + 1
        return ret

def read_in_table_data():
    with open(Constants.TABLE_NAME) as f:
        return {int(splitLine[0]) : splitLine[1] for splitLine in [line.split() for line in f.readlines()]}

def read_in_map_data(buildingIds):
    with open(Constants.MAP_NAME, "rb") as f:
        assert(f.read(15) == b"P5 275 495 255\n")
        rawData = f.readlines()[0]
        return TwoDimRep(rawData), BuildingsRep(buildingIds, rawData)

if __name__ == "__main__":
    buildingTable = read_in_table_data()
    columbia = Village(Constants.MAP_NAME, buildingTable)
    # MapViewer.displayMapWithVillage(columbia)
    MapViewer.displayMapWithVillageSomeColored(columbia, set([9, 161, 255]))
    # twoDimRep, buildingPixelRep = read_in_map_data(buildingTable.keys())
    # twoDimRep.displayTwoDim()
    #bySizeMap = buildingPixelRep.orderBySizeMap()
    #twoDimRep.displayWithHighlightedBuildings(bySizeMap)
