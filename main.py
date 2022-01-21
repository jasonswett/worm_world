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

    MAX_ALLOWED_ORGANISMS = 10
    MIN_ALLOWED_ORGANISMS = 4
    ORGANISM_WIDTH = 6
    CHROMOSOME_LENGTH = 36

    for i in range(0, MAX_ALLOWED_ORGANISMS):
        add_organism(cell_screen, Chromosome(ORGANISM_WIDTH, CHROMOSOME_LENGTH, ''))

    cell_screen.draw_organisms()

    world_time = 0

    while True:
        if random.randint(0, 4) == 0:
            cell = FoodCell(cell_screen)
        else:
            cell = PoisonCell(cell_screen)

        while True:
            touched = False
            for organism in cell_screen.organisms:
                if organism.is_touched_by(cell):
                    organism.react_to(cell)
                    cell_screen.draw_organism(organism)
                    touched = True

            if not(touched):
                cell_screen.draw_cell(cell)

            cell_screen.draw_cell(Cell(cell.previous_x(), cell.y, (0, 0, 0)))

            cell.advance()
            pygame.display.update()

            world_time += 1
            time.sleep(0.001)

            if world_time % 500 == 0:
                for organism in cell_screen.organisms:
                    organism.age()

            for organism in cell_screen.organisms:
                organism.check_health()

            if len(cell_screen.organisms) <= MIN_ALLOWED_ORGANISMS:
                parents = []

                for i in range(0, MIN_ALLOWED_ORGANISMS):
                    for organism in cell_screen.organisms:
                        parents.append(organism)

                while len(cell_screen.organisms) < MAX_ALLOWED_ORGANISMS:
                    add_organism(cell_screen, parents[0].chromosome.offspring_with(parents[1].chromosome))

            if touched:
                break

            if cell.off_screen():
                break

def add_organism(cell_screen, chromosome):
    while True:
        organism_x = random.randint(0, cell_screen.width - 1 - chromosome.width)
        organism_y = random.randint(0, cell_screen.height - 1 - chromosome.height())
        organism_candidate = Organism(cell_screen, (organism_x, organism_y), chromosome)

        if not(organism_candidate.conflicts_with_any_of(cell_screen.organisms)):
            cell_screen.organisms.append(organism_candidate)
            return

main()
