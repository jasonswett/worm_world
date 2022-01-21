from particle_cell import ParticleCell

class FoodCell(ParticleCell):
    def __init__(self, cell_screen):
        self.cell_screen = cell_screen
        self.x = self.cell_screen.width - 1
        self.y = self.cell_screen.random_y()
        self.color = (0, 255, 0)
        self.increment_amount = -1

    def food(self):
        return True

    def off_screen(self):
        return self.x < -1
