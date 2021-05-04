##TODO Write tests for the rotations methods
from cube import Cube
from rotations import Rotations
import numpy as np
import unittest


class TestStringMethods(unittest.TestCase):

    def test_solved_cube(self):
        correct_cube = np.array([[[0, 0, 0],
                                   [0, 0, 0],
                                   [0, 0, 0]],
                                  [[1, 1, 1],
                                   [1, 1, 1],
                                   [1, 1, 1]],
                                  [[2, 2, 2],
                                   [2, 2, 2],
                                   [2, 2, 2]],
                                  [[3, 3, 3],
                                   [3, 3, 3],
                                   [3, 3, 3]],
                                  [[4, 4, 4],
                                   [4, 4, 4],
                                   [4, 4, 4]],
                                  [[5, 5, 5],
                                   [5, 5, 5],
                                   [5, 5, 5]]
                                  ], dtype='uint8')
        solved_cube = Cube.solved_cube()
        equal_arrays = (solved_cube.cube == correct_cube).all()
        self.assertEqual(equal_arrays, True)

    def test_rotate_U(self):
        random_cube = np.array([[[1, 3, 1],
                                 [4, 0, 0],
                                 [1, 3, 3]],
                                [[0, 0, 5],
                                 [1, 1, 1],
                                 [3, 2, 5]],
                                [[2, 1, 4],
                                 [2, 2, 5],
                                 [0, 3, 1]],
                                [[4, 2, 2],
                                 [0, 3, 1],
                                 [1, 3, 1]],
                                [[0, 5, 1],
                                 [4, 4, 4],
                                 [4, 5, 5]],
                                [[4, 0, 2],
                                 [4, 5, 5],
                                 [5, 2, 2]]
                                  ], dtype='uint8')
        random_cube = Cube(random_cube)
        random_cube.rotate('U')
        after_U = np.array(     [[[0, 0, 5],
                                 [4, 0, 0],
                                 [1, 3, 3]],
                                [[2, 1, 4],
                                 [1, 1, 1],
                                 [3, 2, 5]],
                                [[4, 2, 2],
                                 [2, 2, 5],
                                 [0, 3, 1]],
                                [[1, 3, 1],
                                 [0, 3, 1],
                                 [1, 3, 1]],
                                [[4, 4, 0],
                                 [5, 4, 5],
                                 [5, 4, 1]],
                                [[4, 0, 2],
                                 [4, 5, 5],
                                 [5, 2, 2]]
                                  ], dtype='uint8')
        equal_arrays = (random_cube.cube == after_U).all()
        self.assertEqual(equal_arrays, True)

    def test_rotate_U_prime(self):
        random_cube = np.array([[[1, 3, 1],
                                 [4, 0, 0],
                                 [1, 3, 3]],
                                [[0, 0, 5],
                                 [1, 1, 1],
                                 [3, 2, 5]],
                                [[2, 1, 4],
                                 [2, 2, 5],
                                 [0, 3, 1]],
                                [[4, 2, 2],
                                 [0, 3, 1],
                                 [1, 3, 1]],
                                [[0, 5, 1],
                                 [4, 4, 4],
                                 [4, 5, 5]],
                                [[4, 0, 2],
                                 [4, 5, 5],
                                 [5, 2, 2]]
                                  ], dtype='uint8')
        random_cube = Cube(random_cube)
        random_cube.rotate("U'")
        after_U_prime = np.array([[[4, 2, 2],
                                 [4, 0, 0],
                                 [1, 3, 3]],
                                [[1, 3, 1],
                                 [1, 1, 1],
                                 [3, 2, 5]],
                                [[0, 0, 5],
                                 [2, 2, 5],
                                 [0, 3, 1]],
                                [[2, 1, 4],
                                 [0, 3, 1],
                                 [1, 3, 1]],
                                [[1, 4, 5],
                                 [5, 4, 5],
                                 [0, 4, 4]],
                                [[4, 0, 2],
                                 [4, 5, 5],
                                 [5, 2, 2]]
                                  ], dtype='uint8')
        equal_arrays = (random_cube.cube == after_U_prime).all()
        self.assertEqual(equal_arrays, True)

    def test_rotate_R(self):
        random_cube = np.array([[[1, 3, 1],
                                 [4, 0, 0],
                                 [1, 3, 3]],
                                [[0, 0, 5],
                                 [1, 1, 1],
                                 [3, 2, 5]],
                                [[2, 1, 4],
                                 [2, 2, 5],
                                 [0, 3, 1]],
                                [[4, 2, 2],
                                 [0, 3, 1],
                                 [1, 3, 1]],
                                [[0, 5, 1],
                                 [4, 4, 4],
                                 [4, 5, 5]],
                                [[4, 0, 2],
                                 [4, 5, 5],
                                 [5, 2, 2]]
                                  ], dtype='uint8')
        random_cube = Cube(random_cube)
        random_cube.rotate("R")
        print(random_cube.cube)
        # Left column for Back should be the old Right column of Top
        # Right column of Bottom should now be old Left Column of Back
        after_R = np.array(  [[[1, 3, 2],
                               [4, 0, 5],
                               [1, 3, 2]],
                              [[3, 1, 0],
                               [2, 1, 0],
                               [5, 1, 5]],
                              [[1, 1, 4],
                               [4, 2, 5],
                               [5, 3, 1]],
                              [[4, 2, 2],
                               [0, 3, 1],
                               [1, 3, 1]],
                              [[0, 5, 1],
                               [4, 4, 0],
                               [4, 5, 3]],
                              [[4, 0, 2],
                               [4, 5, 2],
                               [5, 2, 0]]
                                  ], dtype='uint8')
        equal_arrays = (random_cube.cube == after_R).all()
        self.assertEqual(equal_arrays, True)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
