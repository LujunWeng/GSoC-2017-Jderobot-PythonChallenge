import numpy



class Universe:
    """The universe of Conway's Game of Life"""

    def __init__(self, dim):
        h, w = dim
        if w < 10 or h < 10:
            w = h = 10

        self.dim = (h, w)
        self.space = numpy.zeros(self.dim)

    def put_life_in(self, pos):
        if self.is_in_space(pos):
            i, j = pos
            self.space[i][j] = 1

    def is_in_space(self, pos):
        i, j = pos
        h, w = self.dim
        if i >= 0 and i < h and j >= 0 and j < w:
            return True
    