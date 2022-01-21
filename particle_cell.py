from cell import Cell

class ParticleCell(Cell):
    def __init__(self, cell_screen):
        self.cell_screen = cell_screen

    def advance(self):
        self.x += self.increment_amount

    def previous_x(self):
        return self.x - self.increment_amount
