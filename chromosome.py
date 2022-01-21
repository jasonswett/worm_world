import random

class Chromosome:
    def __init__(self, width, length, dna_string):
        self.GENE_LENGTH = 2
        self.width = width
        self.length = length
        self.dna_string = dna_string

        if self.dna_string == '':
            for i in range(0, self.width * self.height()):
                self.dna_string += '0' + str(random.randint(0, 1))

    def height(self):
        return int(self.length / self.width)

    def at(self, x, y):
        position_for_cell = (x * self.width + y) * self.GENE_LENGTH
        return self.dna_string[position_for_cell:position_for_cell + self.GENE_LENGTH]

    def offspring_with(self, other_chromosome):
        midway_point = random.randint(0, len(self.dna_string))
        left = self.dna_string[0:midway_point]
        right = other_chromosome.dna_string[midway_point:len(other_chromosome.dna_string)]
        dna_string = left + right

        if random.randint(0, 1) == 0:
            dna_string = self.mutated_dna_string(dna_string)

        return Chromosome(self.width, self.length, dna_string)

    def mutated_dna_string(self, dna_string):
        new_dna_string = dna_string

        for i in range(0, 10):
            bit_index_to_mutate = random.randint(1, len(new_dna_string) - 1)

            if new_dna_string[bit_index_to_mutate] == '0':
                new_character = '1'
            else:
                new_character = '0'

            left = new_dna_string[0:bit_index_to_mutate - 1] + new_character
            right = new_dna_string[bit_index_to_mutate:]
            new_dna_string = left + right

        return new_dna_string
