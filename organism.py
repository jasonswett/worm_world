import random
from cell import Cell
from food_cell import FoodCell
from chromosome import Chromosome

class Organism:
    def __init__(self, cell_screen, position, size):
        self._age = 0

        self.color = (
            random.randint(100, 255),
            0,
            random.randint(100, 255)
        )

        self.cell_screen = cell_screen
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

    def age(self):
        self._age += 1
        if self._age >= 10:
            self.die()

    def advance(self):
        eatable_food_cell = self.eatable_food_cell()

        if eatable_food_cell != None:
            self.eat(eatable_food_cell)

        self.remove_cell(self.oldest_cell())
        self.add_new_cell_at_head()

    def eatable_food_cell(self):
        for cell in self.cells:
            food_cell = cell.adjacent_food_cell(self.cell_screen)
            if food_cell != None:
                return food_cell
        return None

    def eat(self, food_cell):
        self.cell_screen.food_cells.remove(food_cell)
        self.add_new_cell_at_head()
        self._age -= 5

    def add_new_cell_at_head(self):
        number_of_attempts_to_find_unoccupied_space = 0

        while True:
            number_of_attempts_to_find_unoccupied_space += 1
            if number_of_attempts_to_find_unoccupied_space >= 100:
                return

            x_offset = self.offset()
            if x_offset == 0:
                y_offset = [-1, 1][random.randint(0, 1)]
            else:
                y_offset = 0

            x = self.youngest_cell().x + x_offset
            y = self.youngest_cell().y + y_offset
            cell = Cell(x, y, self.color, 0)

            food_cell = self.cell_screen.food_cell_at((cell.x, cell.y))
            if food_cell != None:
                self.eat(food_cell)
                return

            if self.cell_screen.space_available(cell):
                self.age_all_cells()
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
        self.cell_screen.organisms.remove(self)

        for cell in self.cells:
            food_cell = FoodCell((cell.x, cell.y))
            self.cell_screen.food_cells.append(food_cell)
