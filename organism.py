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
        starting_point = self.y
        ending_point = self.size

        for y in range(starting_point, ending_point):
            cell = Cell(self.x, self.y + y, BLUE, ending_point - y)
            self.cells.append(cell)

    def advance(self):
        oldest_cell = self.oldest_cell()
        self.remove_cell(oldest_cell)
        self.age_all_cells()
        self.add_new_cell_at_head()

    def add_new_cell_at_head(self):
        BLUE = (0, 0, 255)
        found_unoccupied_space = False

        while found_unoccupied_space == False:
            x_offset = random.randint(-1, 1)

            if x_offset == 0:
                y_offset = random.randint(-1, 1) # this should really only be -1 OR 1, not 0
            else:
                y_offset = 0

            x = self.youngest_cell().x + x_offset
            y = self.youngest_cell().y + y_offset
            cell = Cell(x, y, BLUE, 0)

            cell_space_conflict = False
            for other_cell in self.cells:
                if cell.occupies_same_space_as(other_cell):
                    cell_space_conflict = True

            if not(cell_space_conflict):
                found_unoccupied_space = True
                self.cells.append(cell)

    def youngest_cell(self):
        youngest_cell = self.cells[0]
        for cell in self.cells:
            if cell.age < youngest_cell.age:
                youngest_cell = cell

        return youngest_cell

    def oldest_cell(self):
        oldest_cell = self.cells[0]
        for cell in self.cells:
            if cell.age > oldest_cell.age:
                oldest_cell = cell

        return oldest_cell

    def remove_cell(self, target_cell):
        original_cells = self.cells
        self.cells = []

        for cell in original_cells:
            if cell != target_cell:
                self.cells.append(cell)

    def age_all_cells(self):
        for cell in self.cells:
            cell.age = cell.age + 1
