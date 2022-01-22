import pygame, time, random, sys
from pygame.locals import *
from cell_screen import CellScreen
from cell import Cell
from food_cell import FoodCell
from poison_cell import PoisonCell
from organism import Organism
from chromosome import Chromosome

def main():
    pygame.init()
    SCREEN_WIDTH = 60
    cell_screen = CellScreen(int(SCREEN_WIDTH * 1.5), SCREEN_WIDTH)
    time.sleep(1)

    MAX_ALLOWED_ORGANISMS = 30
    WORM_SIZE = 8
    for i in range(0, MAX_ALLOWED_ORGANISMS):
        x = random.randint(0, cell_screen.width - 1)
        y = random.randint(0, cell_screen.height - WORM_SIZE - 1)
        cell_screen.organisms.append(Organism((x, y), WORM_SIZE))

    while True:
        cell_screen.clear()

        for organism in cell_screen.organisms:
            if organism.alive:
                organism.advance(cell_screen)
                cell_screen.draw_organism(organism)

        pygame.display.update()
        time.sleep(0.05)

main()
