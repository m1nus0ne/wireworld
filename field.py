from cell import Cell
from config import *
from time import sleep


class Field(object):
    def __init__(self, width: int, height: int, frequency: int,  last_update=None):
        self.width = width
        self.height = height
        self.frequency = frequency

        self.last_update = last_update

    def gen(self, size):
        self.cellSize = size
        self.field: list[list[Cell]] = [[Cell(COLOUR.BLACK, size, (x, y)) for x in range(0, self.height, size)] for y in
                                        range(0, self.width, size)]

    def draw(self):
        for line in self.field:
            for cell in line:
                cell.draw()

    def update(self, current_time):
        if self.frequency != 0:
            if self.last_update - current_time >= self.frequency:
                new_field = self.field.copy()
                for x in range(len(self.field)):
                    for y in range(len(self.field[x])):
                        if self.field[x][y].status == COLOUR.BLACK:
                            pass
                        elif self.field[x][y].status == COLOUR.YELLOW:
                            if checkNear(self.field, x, y):
                                new_field[x][y].status = COLOUR.BLUE
                        elif self.field[x][y].status == COLOUR.BLUE:
                            new_field[x][y].status = COLOUR.RED
                        else:
                            new_field[x][y].status = COLOUR.YELLOW
                    self.field = new_field

    def changeStatus(self, cord: tuple[int, int], new_status: COLOUR):
        x, y = [_ // self.cellSize for _ in cord]
        self.field[y][x].status = new_status


def checkNear(matr: list[list[Cell]], x: int, y: int):
    counter = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            try:
                if matr[x + a][y + b].status == COLOUR.BLUE:
                    if a != 0 and b != 0:
                        counter += 1
            except IndexError:
                pass
    return counter in range(1, 3)
