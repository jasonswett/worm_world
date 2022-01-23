import pygame, time, random, sys
from pygame.locals import *
from cell_screen import CellScreen
from cell import Cell
from food_cell import FoodCell
from poison_cell import PoisonCell
from organism import Organism
from chromosome import Chromosome

def main():
    SCREEN_WIDTH = 60
    MAX_ALLOWED_ORGANISMS = 10
    MIN_ALLOWED_ORGANISMS = 2
    NUMBER_OF_FOOD_CELLS = 200

    pygame.init()

    cell_screen = CellScreen(int(SCREEN_WIDTH * 1.5), SCREEN_WIDTH)

    for i in range(0, MAX_ALLOWED_ORGANISMS):
        chromosome = Chromosome('')
        add_organism(cell_screen, chromosome)

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

        if len(cell_screen.organisms) <= MIN_ALLOWED_ORGANISMS:
            parents = cell_screen.organisms

            while len(cell_screen.organisms) < MAX_ALLOWED_ORGANISMS:
                add_organism(cell_screen, parents[0].chromosome.offspring_with(parents[1].chromosome))

        pygame.display.update()
        time.sleep(0.05)

def add_organism(cell_screen, chromosome):
    worm_size = 4
    x = cell_screen.random_x()
    y = 0

    organism = Organism(
        cell_screen,
        (x, y),
        worm_size,
        chromosome
    )

    cell_screen.organisms.append(organism)

main()
