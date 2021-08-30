import sys
import time
from func import *

import pygame as pg
from config import *
from cell import Cell
from field import Field

field = Field(WIDTH, HEIGHT, 1)
field.gen(CELLSIZE)
last_upd = time.time()
def frq_switch():
    global IsUpd
    if IsUpd:
        IsUpd = False
    else:
        IsUpd = True

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
                frq_switch()
    if time.time() - last_upd >= field.frequency and IsUpd:
        field.update()
        last_upd = time.time()
    field.draw()
    pg.display.flip()
