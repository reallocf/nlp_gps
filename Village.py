from Building import Building
import Constants
from Point import Point
import Utils

class Village():
    def __init__(self, fileName, buildingNameMap):
        self.rawData = self.__pgmToRawData__(fileName)
        self.buildings = self.__constructBuildings__(buildingNameMap, self.rawData)
        self.idToBuildingMap = self.__idToBuildingMap__(self.buildings)

    def getBuildings(self):
        return self.buildings

    def describeBuildingsByShape(self):
        buildingDescriptions = []
        for building in self.buildings:
            buildingDescriptions.append(building.describeBuildingWithShape())
        return buildingDescriptions

    def describeBuildingsByShapeAndLocation(self):
        buildingDescriptions = []
        for building in self.buildings:
            buildingDescriptions.append(building.describeBuildingWithShapeAndLocation())
        return buildingDescriptions

    def describeBuildingsByRelativePositioning(self, relativePositionCheck):
        relativeBuildingMatrix = {}
        for building in self.buildings:
            buildingsRelationsSet = set()
            for otherBuilding in self.buildings:
                if relativePositionCheck(building, otherBuilding):
                    shouldAdd = True
                    for anotherOtherBuilding in self.buildings:
                        if relativePositionCheck(building, anotherOtherBuilding) and relativePositionCheck(anotherOtherBuilding, otherBuilding):
                            shouldAdd = False
                            break
                    if shouldAdd:
                        buildingsRelationsSet.add(otherBuilding)
            relativeBuildingMatrix[building] = buildingsRelationsSet
        return relativeBuildingMatrix

    def __pgmToRawData__(self, fileName):
        with open(Constants.MAP_NAME, "rb") as f:
            assert(f.read(15) == b"P5 275 495 255\n")
            rawData = f.readlines()[0]
            assert(len(rawData) == Constants.WIDTH * Constants.HEIGHT)
            return rawData

    def __constructBuildings__(self, buildingNameMap, rawData):
        idToBuildingPixelMap = {k : [] for k in buildingNameMap}
        for y in range(Constants.HEIGHT):
            for x in range(Constants.WIDTH):
                buildingId = rawData[y * Constants.WIDTH + x]
                assert(buildingId == 0 or buildingId in buildingNameMap)
                if (buildingId != 0):
                    idToBuildingPixelMap[buildingId].append(Point(x, y))
        return [Building(buildingNameMap[buildingId], buildingId, pixels) for buildingId, pixels in idToBuildingPixelMap.items()]

    def __idToBuildingMap__(self, buildings):
        return {building.getId(): building for building in buildings}
