import pygame, time
from cell_screen import CellScreen
from chromosome import Chromosome
from organism import Organism

def main():
    SCREEN_WIDTH = 100
    pygame.init()
    cell_screen = CellScreen(SCREEN_WIDTH, int(SCREEN_WIDTH * 0.618))

    chromosome = Chromosome('')

    organism = Organism(cell_screen, (10, 10), 4, chromosome)

    cell_screen.organisms.append(organism)
    cell_screen.draw_organism(organism)

    pygame.display.update()

    while True:
        time.sleep(0.05)

main()
