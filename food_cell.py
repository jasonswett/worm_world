from cell import Cell

class FoodCell(Cell):
    def __init__(self, position):
        self.color = (0, 255, 0)
        self.x = position[0]
        self.y = position[1]
