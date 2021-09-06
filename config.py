import pygame as pg
from enum import Enum

HEIGHT = 800
WIDTH = 600
CELLSIZE = (40, 40)
FREQUENCY = 1 / 10
SCREEN = pg.display.set_mode((HEIGHT, WIDTH))


class COLOUR(Enum):
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (128, 128, 128)


class STATUS(Enum):
    EMPTY = 0
    TAIL = 1
    HEAD = 2
    CONDUCTOR = 3


colorComparator = {
    STATUS.EMPTY: COLOUR.BLACK,
    STATUS.TAIL: COLOUR.RED,
    STATUS.HEAD: COLOUR.BLUE,
    STATUS.CONDUCTOR: COLOUR.YELLOW,
}