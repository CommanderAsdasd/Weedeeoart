
def rectang(x, y, sizeX, sizeY):
    line(x, y, x+sizeX, y)
    line(x, y, x, y+sizeY)
    line(x+sizeX, y, x, y)
    line(x, y+sizeY, x, y)

def setup():
    rectang(75, 75, 100, 100)
    size(500, 500)
    # line(50, 50, 100, 50)
    # line(50, 50, 50, 150)
    # line(100, 50, 100, 150)
    # line(100, 150, 50, 150)
    # rect(50, 50, 50, 100)

def draw():
    pass
