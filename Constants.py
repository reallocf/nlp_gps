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

RELATIVE_LENGTH_MAGIC_NUM = 5 # "close enough" in left/right vs top/bottom length to the same to be indistinguishable
SIMILARITY_MAGIC_NUM = 25 # number of points that can be missing between mirroring halves of a building for that direction to be considered symmetric