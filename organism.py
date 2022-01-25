import random
from cell import Cell
from food_cell import FoodCell
from chromosome import Chromosome

class Organism:
    REPRODUCTION_THRESHOLD = 4
    DEATH_AGE = 100

    def __init__(self, cell_screen, position, size, chromosome):
        self._age = 0
        self.reproduction_clock = 0

        self.cell_screen = cell_screen
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.chromosome = chromosome
        self.color = self.chromosome.color()

        self.cells = []
        starting_point = self.y
        ending_point = self.y + self.size

        for y in range(starting_point, ending_point):
            cell = Cell(self.x, self.y + y, self.color, ending_point - y)
            cell.age = y
            self.cells.append(cell)

        if random.randint(0, 1) == 0:
            self.reverse()

    def age(self):
        self._age += 1
        if self._age >= self.DEATH_AGE:
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
        if self._age <= 0:
            return

        self.cell_screen.food_cells.remove(food_cell)
        self.add_new_cell_at_head(self.random_movement(), True)
        self._age -= 20
        self.advance_reproduction_clock()

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
                self.age()
                self.reverse()
                return

            x = self.youngest_cell().x + movement[0]
            y = self.youngest_cell().y + movement[1]
            cell = Cell(self.cell_screen.wrapped_x(x), self.cell_screen.wrapped_y(y), self.color, 0)

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

    def reverse(self):
        new_cells = []
        age = 0
        for cell in reversed(self.cells):
            cell.age = age
            new_cells.append(cell)
            age += 1
        self.cells = new_cells

    def advance_reproduction_clock(self):
        if self.reproduction_clock >= self.REPRODUCTION_THRESHOLD:
            #self.color = (255, 0, 0)
            self.color = self.color
        else:
            self.reproduction_clock += 1

    def can_reproduce(self):
        return self.reproduction_clock >= self.REPRODUCTION_THRESHOLD

    def reproduce_with(self, other_organism):
        self.color = self.chromosome.color()
        other_organism.color = other_organism.chromosome.color()
        self.reproduction_clock = 0
        other_organism.reproduction_clock = 0
        return self.chromosome.offspring_with(other_organism.chromosome)

    def die(self):
        self.cell_screen.organisms.remove(self)

        for cell in self.cells:
            food_cell = FoodCell((cell.x, cell.y))
            self.cell_screen.food_cells.append(food_cell)
