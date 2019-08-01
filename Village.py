from Building import Building
import Constants
from Point import Point

class Village():
    def __init__(self, fileName, buildingIds):
        self.rawData = self.__pgmToRawData__(fileName)
        self.buildings = self.__constructBuildings__(buildingIds, self.rawData)
        self.idToBuildingMap = self.__idToBuildingMap__(self.buildings)

    def getBuildings(self):
        return self.buildings

    def __pgmToRawData__(self, fileName):
        with open(Constants.MAP_NAME, "rb") as f:
            assert(f.read(15) == b"P5 275 495 255\n")
            rawData = f.readlines()[0]
            assert(len(rawData) == Constants.WIDTH * Constants.HEIGHT)
            return rawData

    def __constructBuildings__(self, buildingIds, rawData):
        idToBuildingPixelMap = {k : [] for k in buildingIds}
        for y in range(Constants.HEIGHT):
            for x in range(Constants.WIDTH):
                buildingId = rawData[y * Constants.WIDTH + x]
                assert(buildingId == 0 or buildingId in buildingIds)
                if (buildingId != 0):
                    idToBuildingPixelMap[buildingId].append(Point(x, y))
        return [Building(buildingId, pixels) for buildingId, pixels in idToBuildingPixelMap.items()]

    def __idToBuildingMap__(self, buildings):
        return {building.getId(): building for building in buildings}
