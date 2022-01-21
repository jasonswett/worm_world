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

        self.cells = []
        BLUE = (0, 0, 255)

        for y in range(0, 8):
            cell = Cell(self.x, self.y + y, BLUE)
            self.cells.append(cell)
