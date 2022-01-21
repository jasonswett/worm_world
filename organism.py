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

        self.cells = []
        BLUE = (0, 0, 255)

        for y in range(0, self.size):
            age = y
            cell = Cell(self.x, self.y + y, BLUE, age)
            self.cells.append(cell)
