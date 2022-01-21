class Cell:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def occupies_same_space_as(self, other_cell):
        if self.blank() or other_cell.blank():
            return False
        return self.x == other_cell.x and self.y == other_cell.y

    def blank(self):
        return False

    def poison(self):
        return False

    def hurt_by_poison(self):
        return False

    def food(self):
        return False

    def helped_by_food(self):
        return False

    def soft(self):
        return False
