import random

class Chromosome:
    NUMBER_OF_COLOR_BITS = 24
    # Two colors, 8 bits each

    NUMBER_OF_DIRECTION_BITS = 2
    NUMBER_OF_DISTANCE_BITS = 3
    NUMBER_OF_MOVES = 16
    # Movement pattern:
    # - Direction: 2 bits
    # - Distance: 2 bits
    # - Number of "moves": 8
    # - Total: 2 * 2 * 8 = 32

    def __init__(self, dna_string):
        self.dna_string = dna_string

        if self.dna_string == '':
            for i in range(0, self.NUMBER_OF_COLOR_BITS + self.number_of_movement_bits()):
                self.dna_string += str(random.randint(0, 1))

        self.current_movement_index = 0

    def next_movement(self):
        movement = self.movement_pattern()[self.current_movement_index]

        self.current_movement_index += 1
        if self.current_movement_index >= len(self.movement_pattern()):
            self.current_movement_index = 0

        return movement

    def number_of_movement_bits(self):
        return self.NUMBER_OF_MOVES * self.number_of_bits_in_one_movement_specification()

    def number_of_bits_in_one_movement_specification(self):
        return self.NUMBER_OF_DIRECTION_BITS * self.NUMBER_OF_DISTANCE_BITS

    def movement_pattern(self):
        movements = []

        for i in range(0, self.NUMBER_OF_MOVES - 1):
            direction_index = i * self.number_of_bits_in_one_movement_specification()
            direction_binary = self.dna_string[direction_index:direction_index + self.NUMBER_OF_DIRECTION_BITS]
            direction = int(direction_binary, 2)

            distance_index = direction_index + self.NUMBER_OF_DIRECTION_BITS
            distance_binary = self.dna_string[distance_index:distance_index + self.NUMBER_OF_DISTANCE_BITS]
            distance = int(distance_binary, 2) + 1

            for j in range(1, distance):
                movements.append(self.direction_to_xy(direction))

        return movements

    def direction_to_xy(self, direction):
        direction_map = {
            0: [0, -1],
            1: [0, 1],
            2: [1, 0],
            3: [-1, 0]
        }

        return direction_map[direction]

    def color(self):
        red = self.dna_string[0:8]
        blue = self.dna_string[8:16]
        green = self.dna_string[16:24]
        return (int(red, 2), int(green, 2), int(blue, 2))

    def offspring_with(self, other_chromosome):
        midway_point = random.randint(0, len(self.dna_string))
        left = self.dna_string[0:midway_point]
        right = other_chromosome.dna_string[midway_point:len(other_chromosome.dna_string)]
        dna_string = left + right

        if random.randint(0, 1) == 0:
            dna_string = self.mutated_dna_string(dna_string)

        return Chromosome(dna_string)

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
