import pygame as pg
from enum import Enum


class COLOUR(Enum):
    WHITE = (128, 128, 128)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255,255,0)



HEIGHT = 800
WIDTH = 600
CELLSIZE = 40
SCREEN = pg.display.set_mode((HEIGHT, WIDTH))
FREQUENCY = 1/10
IsRunning = True
IsUpd = True