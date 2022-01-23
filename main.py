import pygame, time, random, sys
from pygame.locals import *
from cell_screen import CellScreen
from cell import Cell
from food_cell import FoodCell
from poison_cell import PoisonCell
from organism import Organism
from chromosome import Chromosome

# NEXT:
# Make it so that when two worms touch and they are both
# sufficiently "healthy", they mate

def main():
    SCREEN_WIDTH = 60
    NUMBER_OF_ORGANISMS = 20
    NUMBER_OF_FOOD_CELLS = 100

    pygame.init()

    cell_screen = CellScreen(int(SCREEN_WIDTH * 1.5), SCREEN_WIDTH)

    for i in range(0, NUMBER_OF_ORGANISMS):
        worm_size = random.randint(4, 20)
        x = i * 2
        y = 0
        cell_screen.organisms.append(Organism(cell_screen, (x, y), worm_size))

    for i in range(0, NUMBER_OF_FOOD_CELLS):
        x = cell_screen.random_x()
        y = cell_screen.random_y()
        cell_screen.food_cells.append(FoodCell((x, y)))

    time.sleep(2)

    world_time = 0

    while True:
        cell_screen.clear()

        world_time += 1
        if world_time % 10 == 0:
            for organism in cell_screen.organisms:
                organism.age()

        for food_cell in cell_screen.food_cells:
            cell_screen.draw_cell(food_cell)

        for organism in cell_screen.organisms:
            organism.advance()
            cell_screen.draw_organism(organism)

        pygame.display.update()
        time.sleep(0.05)

main()
