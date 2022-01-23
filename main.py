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

    pygame.init()

    cell_screen = CellScreen(int(SCREEN_WIDTH * 1.5), SCREEN_WIDTH)

    for i in range(0, MAX_ALLOWED_ORGANISMS):
        chromosome = Chromosome('')
        provide_some_food(cell_screen)
        add_organism(cell_screen, chromosome, i)

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

            i = 0
            while len(cell_screen.organisms) < MAX_ALLOWED_ORGANISMS:
                provide_some_food(cell_screen)
                add_organism(cell_screen, parents[0].chromosome.offspring_with(parents[1].chromosome), i)
                i += 1

        pygame.display.update()
        time.sleep(0.05)

def add_organism(cell_screen, chromosome, i):
    worm_size = 4
    x = i * 5
    y = 10

    organism = Organism(
        cell_screen,
        (x, y),
        worm_size,
        chromosome
    )

    cell_screen.organisms.append(organism)

def provide_some_food(cell_screen):
    NUMBER_OF_FOOD_CELLS_PER_ORGANISM = 10
    for i in range(0, NUMBER_OF_FOOD_CELLS_PER_ORGANISM):
        x = cell_screen.random_x()
        y = cell_screen.random_y()
        cell_screen.food_cells.append(FoodCell((x, y)))

main()
