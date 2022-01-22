import random
from cell import Cell
from hard_cell import HardCell
from soft_cell import SoftCell
from blank_cell import BlankCell
from chromosome import Chromosome

class Organism:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.size = 8

        self.refresh_cells()

    def advance(self):
        self.y = self.y + 1
        self.refresh_cells()

    def refresh_cells(self):
        self.cells = []
        BLUE = (0, 0, 255)

        for y in range(self.y, self.y + self.size):
            age = y
            cell = Cell(self.x, self.y + y, BLUE, age)
            self.cells.append(cell)
