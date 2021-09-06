from config import *
import pygame as pg


class Cell(object):
    def __init__(self, status: STATUS, size: tuple[int, int], cord: (int, int)):
        self.status = status
        self.cord = cord
        self.size = size

    def draw(self):
        x, y = self.cord
        pg.draw.rect(surface=SCREEN, color=colorComparator[self.status].value, rect=(x, y, *self.size))
        pg.draw.rect(surface=SCREEN, color=COLOUR.WHITE.value, rect=(x, y, *self.size), width=1)


