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
    SCREEN_WIDTH = 40
    cell_screen = CellScreen(int(SCREEN_WIDTH * 1.5), SCREEN_WIDTH)

    organism = Organism((20, 10))

    cell_screen.draw_organism(organism)
    pygame.display.update()

    while True:
        time.sleep(0.001)

main()
