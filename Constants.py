TABLE_NAME = "data/new-table.txt"
MAP_NAME = "data/new-labeled.pgm"
WIDTH = 275
HEIGHT = 495
BUILDING_NUM = 26
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
YELLOW = (0, 255, 255)
PURPLE = (255, 0, 255)

# "close enough" in left/right vs top/bottom length to the same to be indistinguishable
RELATIVE_LENGTH_MAGIC_NUM = 5

# number of points that can be missing between mirroring halves of a building for that direction to be considered symmetric
SIMILARITY_MAGIC_NUM = 25

# difference between bounding box side lengths determining if skinny/not skinny 
# tuned specifically to separate few remaining groups of buildings that cannot be determined by
# symmetry/orientation/number of bounding box points touching
SKINNINESS_MAGIC_NUM = 40

# difference between small/medium and medium/large buildings
# tuned specifically to separate few remaining groups of buildings that cannot be determined by
# symmetry/orientation/number of bounding box points touching
SMALL_MED_DIVIDE_MAGIC_NUM = 700
MED_LARGE_DIVIDE_MAGIC_NUM = 2000