##TODO Write tests for the rotations methods
from cube import Cube
from rotations import Rotations
import numpy as np
import unittest


class TestStringMethods(unittest.TestCase):

    def test_solved_cube(self):
        random_cube = Cube.random_cube()
        print(random_cube.cube)
        ## This cube should not be possible ^^^


        correct_cube = np.array([[[0, 0],
                                  [0, 0]],
                                 [[1, 1],
                                  [1, 1]],
                                 [[2, 2],
                                  [2, 2]],
                                 [[3, 3],
                                  [3, 3]],
                                 [[4, 4],
                                  [4, 4]],
                                 [[5, 5],
                                  [5, 5]]
                                  ], dtype='uint8')
        solved_cube = Cube.solved_cube()
        equal_arrays = (solved_cube.cube == correct_cube).all()
        self.assertEqual(equal_arrays, True)

    def test_rotate_U(self):
        random_cube = np.array([[[4,2],
                                 [2,1]],
                                [[4,2],
                                 [2,3]],
                                [[4,2],
                                 [5,2]],
                                [[2,2],
                                 [3,1]],
                                [[4,2],
                                 [2,2]],
                                [[4,2],
                                 [5,2]]], dtype='uint8')
        random_cube = Cube(random_cube)
        random_cube.rotate('U')
        after_U = np.array(    [[[4,2],
                                 [2,1]],
                                [[4,2],
                                 [2,3]],
                                [[2,2],
                                 [5,2]],
                                [[4,2],
                                 [3,1]],
                                [[2,4],
                                 [2,2]],
                                [[4,2],
                                 [5,2]]], dtype='uint8')
        equal_arrays = (random_cube.cube == after_U).all()
        self.assertEqual(equal_arrays, True)

    def test_rotate_U_prime(self):
        random_cube = np.array([[[4,2],
                                 [2,1]],
                                [[4,2],
                                 [2,3]],
                                [[4,2],
                                 [5,2]],
                                [[2,2],
                                 [3,1]],
                                [[4,2],
                                 [2,2]],
                                [[4,2],
                                 [5,2]]], dtype='uint8')
        random_cube = Cube(random_cube)
        random_cube.rotate("U'")
        after_U_prime = np.array([[[2,2],
                                   [2,1]],
                                  [[4,2],
                                   [2,3]],
                                  [[4,2],
                                   [5,2]],
                                  [[4,2],
                                   [3,1]],
                                  [[2,2],
                                   [4,2]],
                                  [[4,2],
                                   [5,2]]], dtype='uint8')
        equal_arrays = (random_cube.cube == after_U_prime).all()
        self.assertEqual(equal_arrays, True)

    # def test_rotate_R(self):
    #     random_cube = np.array([[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     random_cube = Cube(random_cube)
    #     random_cube.rotate("R")
    #     # Left column for Back should be the old Right column of Top
    #     # Right column of Bottom should now be old Left Column of Back
    #     after_R = np.array(  [[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     equal_arrays = (random_cube.cube == after_R).all()
    #     self.assertEqual(equal_arrays, True)
    #
    # def test_rotate_R_prime(self):
    #     random_cube = np.array([[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     random_cube = Cube(random_cube)
    #     random_cube.rotate("R'")
    #     # Left column for Back should be the old Right column of Bottom
    #     # Right column of Top should now be old Left Column of Back
    #     after_R_prime = np.array([[[4,2],
    #                                [2,1]],
    #                               [[4,2],
    #                                [2,3]],
    #                               [[4,2],
    #                                [5,2]],
    #                               [[2,2],
    #                                [3,1]],
    #                               [[4,2],
    #                                [2,2]],
    #                               [[4,2],
    #                                [5,2]]], dtype='uint8')
    #     equal_arrays = (random_cube.cube == after_R_prime).all()
    #     self.assertEqual(equal_arrays, True)
    #
    # def test_rotate_L(self):
    #     random_cube = np.array([[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     random_cube = Cube(random_cube)
    #     random_cube.rotate("L")
    #     after_L = np.array([[[4,2],
    #                          [2,1]],
    #                         [[4,2],
    #                          [2,3]],
    #                         [[4,2],
    #                          [5,2]],
    #                         [[2,2],
    #                          [3,1]],
    #                         [[4,2],
    #                          [2,2]],
    #                         [[4,2],
    #                          [5,2]]], dtype='uint8')
    #     equal_arrays = (random_cube.cube == after_L).all()
    #     self.assertEqual(equal_arrays, True)
    #
    #
    # def test_rotate_L_prime(self):
    #     random_cube = np.array([[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     random_cube = Cube(random_cube)
    #     random_cube.rotate("L'")
    #     after_L_prime = np.array([[[4,2],
    #                                [2,1]],
    #                               [[4,2],
    #                                [2,3]],
    #                               [[4,2],
    #                                [5,2]],
    #                               [[2,2],
    #                                [3,1]],
    #                               [[4,2],
    #                                [2,2]],
    #                               [[4,2],
    #                                [5,2]]], dtype='uint8')
    #     equal_arrays = (random_cube.cube == after_L_prime).all()
    #     self.assertEqual(equal_arrays, True)
    #
    # def test_rotate_D(self):
    #     random_cube = np.array([[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     random_cube = Cube(random_cube)
    #     random_cube.rotate("D")
    #     after_D = np.array([[[4,2],
    #                          [2,1]],
    #                         [[4,2],
    #                          [2,3]],
    #                         [[4,2],
    #                          [5,2]],
    #                         [[2,2],
    #                          [3,1]],
    #                         [[4,2],
    #                          [2,2]],
    #                         [[4,2],
    #                          [5,2]]], dtype='uint8')
    #     equal_arrays = (random_cube.cube == after_D).all()
    #     self.assertEqual(equal_arrays, True)
    #
    # def test_rotate_D_prime(self):
    #     random_cube = np.array([[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     random_cube = Cube(random_cube)
    #     random_cube.rotate("D'")
    #     after_D_prime = np.array([[[4,2],
    #                                [2,1]],
    #                               [[4,2],
    #                                [2,3]],
    #                               [[4,2],
    #                                [5,2]],
    #                               [[2,2],
    #                                [3,1]],
    #                               [[4,2],
    #                                [2,2]],
    #                               [[4,2],
    #                                [5,2]]], dtype='uint8')
    #     equal_arrays = (random_cube.cube == after_D_prime).all()
    #     self.assertEqual(equal_arrays, True)
    #
    # def test_rotate_F(self):
    #     random_cube = np.array([[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     random_cube = Cube(random_cube)
    #     random_cube.rotate("F")
    #     after_F = np.array([[[4,2],
    #                          [2,1]],
    #                         [[4,2],
    #                          [2,3]],
    #                         [[4,2],
    #                          [5,2]],
    #                         [[2,2],
    #                          [3,1]],
    #                         [[4,2],
    #                          [2,2]],
    #                         [[4,2],
    #                          [5,2]]], dtype='uint8')
    #     equal_arrays = (random_cube.cube == after_F).all()
    #     self.assertEqual(equal_arrays, True)
    #
    # def test_rotate_F_prime(self):
    #     random_cube = np.array([[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     random_cube = Cube(random_cube)
    #     random_cube.rotate("F'")
    #     after_F_prime = np.array([[[4,2],
    #                                [2,1]],
    #                               [[4,2],
    #                                [2,3]],
    #                               [[4,2],
    #                                [5,2]],
    #                               [[2,2],
    #                                [3,1]],
    #                               [[4,2],
    #                                [2,2]],
    #                               [[4,2],
    #                                [5,2]]], dtype='uint8')
    #     equal_arrays = (random_cube.cube == after_F_prime).all()
    #     self.assertEqual(equal_arrays, True)
    #
    # def test_rotate_B(self):
    #     random_cube = np.array([[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     random_cube = Cube(random_cube)
    #     random_cube.rotate("B")
    #     after_B = np.array([[[4,2],
    #                          [2,1]],
    #                         [[4,2],
    #                          [2,3]],
    #                         [[4,2],
    #                          [5,2]],
    #                         [[2,2],
    #                          [3,1]],
    #                         [[4,2],
    #                          [2,2]],
    #                         [[4,2],
    #                          [5,2]]], dtype='uint8')
    #     equal_arrays = (random_cube.cube == after_B).all()
    #     self.assertEqual(equal_arrays, True)
    #
    # def test_rotate_B_prime(self):
    #     random_cube = np.array([[[4,2],
    #                              [2,1]],
    #                             [[4,2],
    #                              [2,3]],
    #                             [[4,2],
    #                              [5,2]],
    #                             [[2,2],
    #                              [3,1]],
    #                             [[4,2],
    #                              [2,2]],
    #                             [[4,2],
    #                              [5,2]]], dtype='uint8')
    #     random_cube = Cube(random_cube)
    #     random_cube.rotate("B'")
    #     after_B_prime = np.array([[[4,2],
    #                                [2,1]],
    #                               [[4,2],
    #                                [2,3]],
    #                               [[4,2],
    #                                [5,2]],
    #                               [[2,2],
    #                                [3,1]],
    #                               [[4,2],
    #                                [2,2]],
    #                               [[4,2],
    #                                [5,2]]], dtype='uint8')
    #     equal_arrays = (random_cube.cube == after_B_prime).all()
    #     self.assertEqual(equal_arrays, True)


if __name__ == '__main__':
    unittest.main()
