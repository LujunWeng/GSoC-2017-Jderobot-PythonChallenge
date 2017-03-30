from unittest import TestCase
import numpy
from modules.conway import Universe


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

    def test_next_generation(self):
        # Test 4 life rules
        # Live cell with fewer than two live neighbours dies
        u = Universe((10, 10))
        u.put_life_in((0, 0))
        u.put_life_in((0, 1))
        u.next_generation()
        actual = numpy.zeros((10, 10))
        numpy.testing.assert_array_equal(u.space, actual)

        # Live cell with two or three ive neighbours live
        # Any dead cell with exactly three live neighbours live
        u = Universe((10, 10))
        u.put_life_in((0, 0))
        u.put_life_in((0, 1))
        u.put_life_in((1, 0))
        u.next_generation()
        actual = numpy.zeros((10, 10))
        actual[0][0] = 1
        actual[0][1] = 1
        actual[1][0] = 1
        actual[1][1] = 1
        numpy.testing.assert_array_equal(u.space, actual)
        u.next_generation()
        numpy.testing.assert_array_equal(u.space, actual)

        # Live cell with more than three live neighbours dies
        u = Universe((10, 10))
        u.put_life_in((0, 0))
        u.put_life_in((0, 1))
        u.put_life_in((1, 1))
        u.put_life_in((1, 0))
        u.put_life_in((2, 0))
        u.next_generation()
        actual = numpy.zeros((10, 10))
        actual[0][0] = 1
        actual[0][1] = 1
        actual[2][0] = 1
        actual[2][1] = 1
        numpy.testing.assert_array_equal(u.space, actual)

    def test_number_of_neighbours(self):
        u = Universe((10, 10))
        self.assertEqual(0, u.number_of_neighbours((0, 0)))
        u.put_life_in((0, 1))
        self.assertEqual(1, u.number_of_neighbours((0, 0)))
        u.put_life_in((1, 1))
        self.assertEqual(2, u.number_of_neighbours((0, 0)))
        u.put_life_in((1, 0))
        self.assertEqual(3, u.number_of_neighbours((0, 0)))

        u = Universe((10, 10))
        self.assertEqual(0, u.number_of_neighbours((1, 1)))
        u.put_life_in((0, 1))
        self.assertEqual(1, u.number_of_neighbours((1, 1)))
        u.put_life_in((0, 0))
        self.assertEqual(2, u.number_of_neighbours((1, 1)))
        u.put_life_in((1, 0))
        self.assertEqual(3, u.number_of_neighbours((1, 1)))


    def test_random_reset(self):
        u = Universe((10, 10))
        try:
            u.random_reset(10000)
        except ValueError:
            self.fail("random_reset(10000) raised ValueError")
