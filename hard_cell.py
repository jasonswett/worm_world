from cell import Cell

class HardCell(Cell):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 0)
