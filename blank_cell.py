from cell import Cell

class BlankCell(Cell):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 0, 0)

    def hurt_by_poison(self):
        return False

    def blank(self):
        return True
