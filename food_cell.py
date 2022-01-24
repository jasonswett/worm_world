import random
from cell import Cell

class FoodCell(Cell):
    def __init__(self, position):
        self.color = (0, 255, 0)
        self.age = 0
        self.x = position[0]
        self.y = position[1]

    def move(self):
        self.age += 1
        if random.randint(0, 9) != 0 or self.age < 100:
            return
        movement = self.random_movement()
        self.x += movement[0]
        self.y += movement[1]

    def random_movement(self):
        random_offset = [-1, 1][random.randint(0, 1)]

        if random.randint(0, 1) == 0:
            return [random_offset, 0]
        else:
            return [0, random_offset]
