from particle_cell import ParticleCell

class PoisonCell(ParticleCell):
    def __init__(self, cell_screen):
        self.cell_screen = cell_screen
        self.x = 0
        self.y = self.cell_screen.random_y()
        self.color = (255, 0, 0)
        self.increment_amount = 1

    def poison(self):
        return True

    def off_screen(self):
        return self.x >= self.cell_screen.width + 1
