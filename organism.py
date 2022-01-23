import random
from cell import Cell
from food_cell import FoodCell
from chromosome import Chromosome

class Organism:
    def __init__(self, cell_screen, position, size, chromosome):
        self._age = 0

        self.cell_screen = cell_screen
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.chromosome = chromosome
        self.color = self.chromosome.color()

        self.cells = []
        starting_point = self.y
        ending_point = self.y + self.size

        self.bias_toward_straight_movement = random.uniform(0, 1)

        for y in range(starting_point, ending_point):
            cell = Cell(self.x, self.y + y, self.color, ending_point - y)
            self.cells.append(cell)

    def age(self):
        self._age += 1
        if self._age >= 100:
            self.die()

    def advance(self):
        if len(self.cells) <= 3:
            self.die()

        eatable_food_cell = self.eatable_food_cell()

        if eatable_food_cell != None:
            self.eat(eatable_food_cell)

        self.add_new_cell_at_head(self.movement(), False)

    def eatable_food_cell(self):
        for cell in self.cells:
            food_cell = cell.adjacent_food_cell(self.cell_screen)
            if food_cell != None:
                return food_cell
        return None

    def eat(self, food_cell):
        self.cell_screen.food_cells.remove(food_cell)
        self.add_new_cell_at_head(self.random_movement(), True)
        self._age -= 5

    def movement(self):
        return self.chromosome.next_movement()

    def random_movement(self):
        random_offset = [-1, 1][random.randint(0, 1)]

        if random.randint(0, 1) == 0:
            return [random_offset, 0]
        else:
            return [0, random_offset]

    def add_new_cell_at_head(self, movement, grow):
        number_of_attempts_to_find_unoccupied_space = 0

        if movement[0] == 0 and movement[1] == 0:
            return

        while True:
            number_of_attempts_to_find_unoccupied_space += 1

            if number_of_attempts_to_find_unoccupied_space >= 2:
                movement = self.random_movement()

            if number_of_attempts_to_find_unoccupied_space >= 100:
                self.die()
                return

            x = self.youngest_cell().x + movement[0]
            y = self.youngest_cell().y + movement[1]
            cell = Cell(x, y, self.color, 0)

            food_cell = self.cell_screen.food_cell_at((cell.x, cell.y))
            if food_cell != None:
                self.eat(food_cell)
                return

            if self.cell_screen.space_available(cell):
                self.age_all_cells()
                if not(grow):
                    self.age()
                    self.remove_cell(self.oldest_cell())
                self.cells.append(cell)
                return

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
