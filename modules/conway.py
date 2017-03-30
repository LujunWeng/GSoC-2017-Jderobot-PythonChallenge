import random
import numpy


class Universe:
    """The universe of Conway's Game of Life"""
    NEIGHBOURS_SHIFT = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1), (0, 1),
                        (1, -1), (1, 0), (1, 1)]

    def __init__(self, dim):
        h, w = dim
        # Minimum size
        if w < 10 or h < 10:
            w = h = 10

        self.dim = (h, w)
        self.space = numpy.zeros(self.dim)
        self.generation = 0

    def put_life_in(self, pos):
        if self.is_in_space(pos):
            i, j = pos
            self.space[i][j] = 1

    def is_in_space(self, pos):
        i, j = pos
        h, w = self.dim
        if i >= 0 and i < h and j >= 0 and j < w:
            return True

    def next_generation(self):
        new_space = numpy.zeros(self.dim)
        for i in range(len(self.space)):
            for j in range(len(self.space[i])):
                n = self.number_of_neighbours((i, j))
                if self.space[i][j] == 1:
                    if n < 2:
                        new_space[i][j] = 0
                    elif 2 <= n <= 3:
                        new_space[i][j] = 1
                    else:
                        new_space[i][j] = 0
                else:
                    if n == 3:
                        new_space[i][j] = 1
                    else:
                        new_space[i][j] = 0

        self.space = new_space.copy()
        self.generation += 1

    def number_of_neighbours(self, pos):
        cnt = 0
        for shift in self.NEIGHBOURS_SHIFT:
            i = pos[0] + shift[0]
            j = pos[1] + shift[1]
            if self.is_in_space((i, j)) and self.space[i][j] == 1:
                cnt += 1
        return cnt

    def clear_universe(self):
        self.space = numpy.zeros(self.dim)

    def random_reset(self, nlives):
        h, w = self.dim
        ncells = h * w
        # if the number of seeds is greater than the number of cells
        if nlives > ncells:
            ncells = nlives
        poss = random.sample(range(ncells), nlives)
        self.clear_universe()
        for p in poss:
            i = p % h
            j = numpy.math.floor(p / h)
            self.put_life_in((i, j))
        self.generation = 0
