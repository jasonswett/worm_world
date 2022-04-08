import pygame, time, random, sys
from pygame.locals import *
from cell_screen import CellScreen
from cell import Cell
from food_cell import FoodCell
from organism import Organism
from chromosome import Chromosome

def main():
    SCREEN_WIDTH = 100
    MAX_ALLOWED_ORGANISMS = 10

    pygame.init()

    cell_screen = CellScreen(SCREEN_WIDTH, int(SCREEN_WIDTH * 0.618))

    for i in range(0, MAX_ALLOWED_ORGANISMS):
        chromosome = Chromosome('')
        provide_some_food(cell_screen)
        add_organism(cell_screen, chromosome)

    time.sleep(2)

    world_time = 0

    while True:
        world_time += 1
        cell_screen.clear()

        for food_cell in cell_screen.food_cells:
            food_cell.move()
            cell_screen.draw_cell(food_cell)

        for organism in cell_screen.organisms:
            organism.advance()
            cell_screen.draw_organism(organism)

        pygame.display.update()

        for organism in cell_screen.organisms:
            adjacent_organism = cell_screen.adjacent_organism(organism)
            if adjacent_organism != None and organism.can_reproduce() and adjacent_organism.can_reproduce():
                for i in range(0, 3):
                    chromosome = organism.reproduce_with(adjacent_organism)
                    add_organism(cell_screen, chromosome)

        pygame.display.update()
        time.sleep(0.5)

def add_organism(cell_screen, chromosome):
    organism = Organism(
        cell_screen,
        (cell_screen.random_x(), cell_screen.random_y()),
        4,
        chromosome
    )

    cell_screen.organisms.append(organism)

def provide_some_food(cell_screen):
    NUMBER_OF_FOOD_CELLS_PER_ORGANISM = 20
    for i in range(0, NUMBER_OF_FOOD_CELLS_PER_ORGANISM):
        x = cell_screen.random_x()
        y = cell_screen.random_y()
        cell_screen.food_cells.append(FoodCell((x, y)))

main()
