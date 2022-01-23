import random

class Chromosome:
    def __init__(self):
        self.dna_string = ''

        for i in range(0, 16):
            self.dna_string += str(random.randint(0, 1))

        print(self.dna_string)

    def color(self):
        red = '1' + self.dna_string[1:8]
        blue = '1' + self.dna_string[9:16]
        return (int(red, 2), 0, int(blue, 2))

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
