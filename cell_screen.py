import pygame, random

INNER_CELL_WIDTH = 6
CELL_WIDTH = INNER_CELL_WIDTH + 2

class CellScreen:
    def __init__(self, width, height):
        self.organisms = []
        self.food_cells = []

        self.width = width
        self.height = height

        width_in_pixels = CELL_WIDTH * width
        height_in_pixels = CELL_WIDTH * height
        self.display = pygame.display.set_mode((width_in_pixels, height_in_pixels), 0, 32)

    def clear(self):
        self.display.fill((0, 0, 0))

    def draw_cell(self, cell):
        x_position = cell.x * CELL_WIDTH
        y_position = cell.y * CELL_WIDTH
        pygame.draw.rect(self.display, cell.color, (x_position, y_position, INNER_CELL_WIDTH, INNER_CELL_WIDTH), 0)

    def draw_organism(self, organism):
        for cell in organism.cells:
            self.draw_cell(cell)

    def random_x(self):
        return random.randint(0, self.width - 1)

    def random_y(self):
        return random.randint(0, self.height - 1)

    def wrapped_x(self, x):
        if x >= self.width:
            return x - self.width
        elif x < 0:
            return x + self.width
        else:
            return x

    def wrapped_y(self, y):
        if y >= self.height:
            return y - self.height
        elif y < 0:
            return y + self.height
        else:
            return y

    def draw_organisms(self):
        for organism in self.organisms:
            self.draw_organism(organism)
        pygame.display.update()

    def remove_organism(self, organism):
        for i, self_organism in enumerate(self.organisms):
            if self_organism == organism:
                del self.organisms[i]

    def space_available(self, cell):
        if cell.y < 0:
            return False
        if cell.x < 0:
            return False
        if cell.y >= self.height:
            return False
        if cell.x >= self.width:
            return False

        for other_cell in self.other_cells():
            if cell.occupies_same_space_as(other_cell):
                return False

        return True

    def other_cells(self):
        cells = []

        for organism in self.organisms:
            for cell in organism.cells:
                cells.append(cell)

        for cell in self.food_cells:
            cells.append(cell)

        return cells

    def food_cell_at(self, position):
        x = position[0]
        y = position[1]

        for food_cell in self.food_cells:
            if food_cell.x == x and food_cell.y == y:
                return food_cell
        return None

    def adjacent_organism(self, organism):
        for other_organism in self.organisms:
            for other_cell in other_organism.cells:
                for cell in organism.cells:
                    if other_cell.adjacent_to(cell) and organism != other_organism:
                        return other_organism
        return None
