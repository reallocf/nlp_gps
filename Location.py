import Constants

'''
Map broken down into 9 sections:
 -----------------------
|       |       |       |
|       |       |       |
|       |       |       |
|       |       |       |
|       |       |       |
|-----------------------|
|       |       |       |
|       |       |       |
|       |       |       |
|       |       |       |
|       |       |       |
|-----------------------|
|       |       |       |
|       |       |       |
|       |       |       |
|       |       |       |
|       |       |       |
 -----------------------
'''
class Location:
    def __init__(self, center):
        self.center = center
        self.xDirectionThird = self.__calcXDirectionThird__(self.center)
        self.yDirectionThird = self.__calcYDirectionThird__(self.center)

    def __repr__(self):
        if self.xDirectionThird == "center" and self.yDirectionThird == "center":
            return "in the center"
        else:
            return f'in the {self.yDirectionThird} {self.xDirectionThird}'

    def __calcXDirectionThird__(self, center):
        if center.x < Constants.WIDTH / 3.0:
            return "left"
        elif center.x < 2 * Constants.WIDTH / 3.0:
            return "center"
        else:
            return "right"

    def __calcYDirectionThird__(self, center):
        if center.y < Constants.WIDTH / 3.0:
            return "upper"
        elif center.y < 2 * Constants.WIDTH / 3.0:
            return "center"
        else:
            return "bottom"

    '''
    For North, South, East, West, it is based not on the center simply being above, but it must be above in a triangle
    of configurable angle degrees. Diagram key: (C = Center, X = North, . = not North)
    .XXXXXXX.
    ..XXXXX..
    ..XXXXX..
    ...XXX...
    ...XXX...
    ....C....
    .........
    There are similar triangle for each other direction.
    '''
    def isItNorth(self, otherLoc):
        xDiff = otherLoc.center.x - self.center.x
        yDiff = otherLoc.center.y - self.center.y
        return (yDiff * Constants.DIRECTION_ANGLE_MAGIC_NUM - xDiff < 0) and (yDiff * Constants.DIRECTION_ANGLE_MAGIC_NUM + xDiff < 0)

    def isItSouth(self, otherLoc):
        xDiff = otherLoc.center.x - self.center.x
        yDiff = otherLoc.center.y - self.center.y
        return (yDiff * Constants.DIRECTION_ANGLE_MAGIC_NUM - xDiff > 0) and (yDiff * Constants.DIRECTION_ANGLE_MAGIC_NUM + xDiff > 0)

    def isItEast(self, otherLoc):
        xDiff = otherLoc.center.x - self.center.x
        yDiff = otherLoc.center.y - self.center.y
        return (yDiff - Constants.DIRECTION_ANGLE_MAGIC_NUM * xDiff < 0) and (yDiff + Constants.DIRECTION_ANGLE_MAGIC_NUM * xDiff > 0)

    def isItWest(self, otherLoc):
        xDiff = otherLoc.center.x - self.center.x
        yDiff = otherLoc.center.y - self.center.y
        return (yDiff - Constants.DIRECTION_ANGLE_MAGIC_NUM * xDiff > 0) and (yDiff + Constants.DIRECTION_ANGLE_MAGIC_NUM * xDiff < 0)
