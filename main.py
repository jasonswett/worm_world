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

    cell_screen.organisms = [
        Organism((20, 0)),
        Organism((30, 0)),
        Organism((40, 0)),
        Organism((50, 0)),
        Organism((60, 0)),
        Organism((70, 0)),
    ]

    while True:
        cell_screen.clear()

        for organism in cell_screen.organisms:
            if organism.alive:
                organism.advance(cell_screen)
                cell_screen.draw_organism(organism)

        pygame.display.update()
        time.sleep(0.1)

main()
