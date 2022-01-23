import random
from cell import Cell
from hard_cell import HardCell
from soft_cell import SoftCell
from blank_cell import BlankCell
from chromosome import Chromosome

class Organism:
    def __init__(self, position, size):
        self.alive = True

        self.color = (
            random.randint(100, 255),
            0,
            random.randint(100, 255)
        )

        self.x = position[0]
        self.y = position[1]
        self.size = size

        self.cells = []
        starting_point = self.y
        ending_point = self.y + self.size

        self.bias_toward_straight_movement = random.uniform(0, 1)

        for y in range(starting_point, ending_point):
            cell = Cell(self.x, self.y + y, self.color, ending_point - y)
            self.cells.append(cell)

    def advance(self, cell_screen):
        self.remove_cell(self.oldest_cell())
        self.age_all_cells()
        self.add_new_cell_at_head(cell_screen)

    def add_new_cell_at_head(self, cell_screen):
        number_of_attempts_to_find_unoccupied_space = 0

        while True:
            number_of_attempts_to_find_unoccupied_space += 1
            if number_of_attempts_to_find_unoccupied_space >= 100:
                self.die()
                return

            x_offset = self.offset()
            if x_offset == 0:
                y_offset = [-1, 1][random.randint(0, 1)]
            else:
                y_offset = 0

            x = self.youngest_cell().x + x_offset
            y = self.youngest_cell().y + y_offset
            cell = Cell(x, y, self.color, 0)

            if cell_screen.space_available(cell):
                self.cells.append(cell)
                return

    def offset(self):
        raw_offset = random.uniform(0, 1)
        if raw_offset > self.bias_toward_straight_movement:
            offset = 0
        else:
            offset = 1

        x_modifier = [-1, 1][random.randint(0, 1)]
        offset *= x_modifier
        return offset


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

    def die(self):
        self.alive = False
