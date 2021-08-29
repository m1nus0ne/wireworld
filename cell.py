from config import *


class Cell(object):
    def __init__(self, status: COLOUR, size : int, cord : (int,int)):
        self.status = status
        self.size = size
        self.cord = cord

    def draw(self):
        x,y = self.cord
        pg.draw.rect(surface=SCREEN, color=self.status.value, rect=(x,y,self.size,self.size))
        pg.draw.rect(surface=SCREEN, color=self.status.value, rect=(x,y,self.size,self.size),width=2)


