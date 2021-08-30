from config import IsUpd, COLOUR


def checkNear(matr, x: int, y: int):
    counter = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            try:
                if matr[x + a][y + b] == 1 and not(a==0 and b==0):
                    counter += 1
            except IndexError:
                pass
    return counter in range(1, 4)

matr = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for x in range(3):
    for y in range(3):
        print(checkNear(matr,x,y))