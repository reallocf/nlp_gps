class Description:
    def __init__(self):
        self.descriptors = []

    def __repr__(self):
        return "is " + " and is ".join(self.descriptors)

    def isRectangular(self):
        self.descriptors.append("rectangular")

    def isDoubleSymmetricNotRectangular(self):
        self.descriptors.append("double symmetric but not rectangular")

    def isOnlyLeftRightSymmetric(self):
        self.descriptors.append("only left-right symmetric")

    def isOnlyTopBottomSymmetric(self):
        self.descriptors.append("only top-bottom symmetric")

    def isNotSymmetric(self):
        self.descriptors.append("not symmetric")

    def isLongerLeftRight(self):
        self.descriptors.append("longer left-right than top-bottom")

    def isLongerTopBottom(self):
        self.descriptors.append("longer top-bottom than left-right")

    def isLengthSameLeftRightTopBottom(self):
        self.descriptors.append("the same top-bottom and left-right")

    def touchesOnXBoundingBoxCorners(self, cornerCount):
        if cornerCount == 1:
            self.descriptors.append("touching the bounding box on 1 corner")
        else:
            self.descriptors.append("touching the bounding box on " + str(cornerCount) + " corners")

    def isSkinny(self):
        self.descriptors.append("skinny")

    def isNotSkinny(self):
        self.descriptors.append("not skinny")

    def isSmall(self):
        self.descriptors.append("small")

    def isMedium(self):
        self.descriptors.append("medium")

    def isLarge(self):
        self.descriptors.append("large")
