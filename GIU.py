import sys
import time

import pygame as pg
from config import *
from cell import Cell
from field import Field

field = Field(WIDTH, HEIGHT, 10, 0)
field.gen(CELLSIZE)

while IsRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            IsRunning = False
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                field.changeStatus(pg.mouse.get_pos(), COLOUR.BLACK)
            if event.key == pg.K_2:
                field.changeStatus(pg.mouse.get_pos(), COLOUR.YELLOW)
            if event.key == pg.K_3:
                field.changeStatus(pg.mouse.get_pos(), COLOUR.BLUE)
            if event.key == pg.K_4:
                field.changeStatus(pg.mouse.get_pos(), COLOUR.RED)
            if event.key == pg.K_SPACE:
                field.frequency = 0
    field.update(time.time())
    field.draw()
    pg.display.flip()
