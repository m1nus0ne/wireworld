from cell import Cell
from config import *
from copy import deepcopy


class Field(object):
    def __init__(self, width: int, height: int, cellsize: tuple[int, int]):
        self.width = width
        self.height = height
        self.cellsize = cellsize
        self.field = [[Cell(STATUS.EMPTY, cellsize, (x, y)) for x in range(0, self.height, cellsize[0])] for y in range(0, self.width, cellsize[1])]

    def draw(self):
        for line in self.field:
            for cell in line:
                cell.draw()

    def update(self):
        new_field = deepcopy(self.field)
        for x in range(len(self.field)):
            for y in range(len(self.field[x])):
                if self.field[x][y].status == STATUS.CONDUCTOR:
                    if self.checkNear(x, y):
                        new_field[x][y].status = STATUS.HEAD
                elif self.field[x][y].status == STATUS.HEAD:
                    new_field[x][y].status = STATUS.TAIL
                elif self.field[x][y].status == STATUS.TAIL:
                    new_field[x][y].status = STATUS.CONDUCTOR
        self.field = deepcopy(new_field)

    def changeStatus(self, cord: tuple[int, int], status: STATUS):
        x, y = [cord[i] // self.cellsize[i] for i in range(2)]
        self.field[y][x].status = status

    def checkNear(self, x: int, y: int):
        counter = 0
        for a in range(-1, 2):
            for b in range(-1, 2):
                try:
                    if self.field[x + a][y + b].status == STATUS.HEAD and not (a == 0 and b == 0):
                        counter += 1
                except IndexError:
                    pass
        return counter in range(1, 3)
