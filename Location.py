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
