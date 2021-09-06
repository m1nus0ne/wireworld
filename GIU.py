import sys
import time

from config import *
from field import Field

field = Field(WIDTH, HEIGHT, CELLSIZE)
last_upd = time.time()

isRunning = True
isUpd = True

while isRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
            sys.exit()
        elif event.type == pg.KEYDOWN:
            pos = pg.mouse.get_pos()
            if event.key == pg.K_1:
                field.changeStatus(pos, STATUS.EMPTY)
            elif event.key == pg.K_2:
                field.changeStatus(pos, STATUS.CONDUCTOR)
            elif event.key == pg.K_3:
                field.changeStatus(pos, STATUS.HEAD)
            elif event.key == pg.K_4:
                field.changeStatus(pos, STATUS.TAIL)
            elif event.key == pg.K_SPACE:
                isUpd = not isUpd
    if time.time() - last_upd >= FREQUENCY and isUpd:
        field.update()
        last_upd = time.time()
    field.draw()
    pg.display.flip()
