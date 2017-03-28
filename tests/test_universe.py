from unittest import TestCase

import numpy

from conway import Universe

class TestUniverse(TestCase):
    def test_created_earth(self):

        # Minimum size is 10 x 10
        eu = Universe((1, 2))
        au = numpy.zeros((10, 10))
        numpy.testing.assert_array_equal(eu.space, au)

        # Create a normal universe
        eu = Universe((11, 12))
        au = numpy.zeros((11, 12))
        numpy.testing.assert_array_equal(eu.space, au)

    def test_put_life_in(self):
        # Life position is within the universe
        eu = Universe((10, 10))
        au = numpy.zeros((10, 10))
        au[2][3] = 1
        eu.put_life_in((2, 3))
        numpy.testing.assert_array_equal(eu.space, au)

        # Life position is out of the universe
        eu = Universe((10, 10))
        au = numpy.zeros((10, 10))
        eu.put_life_in((11, 9))
        numpy.testing.assert_array_equal(eu.space, au)
