from cell import Cell

class SoftCell(Cell):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 0, 255)

    def hurt_by_poison(self):
        return True

    def helped_by_food(self):
        return True

    def soft(self):
        return True
