import numpy as np


class Rotations:
    @staticmethod
    def U(cube):
        # rotating the top row
        temp = cube[0, 0, :].copy()
        for i in range(cube.shape[1]):
            cube[i, 0, :] = cube[i + 1, 0, :]
        cube[3, 0, :] = temp
        # rotating the upper side
        temp = cube[4, 0, :].copy()
        cube[4, 0, :] = np.flip(cube[4, :, 0])
        cube[4, :, 0] = cube[4, cube.shape[1] - 1, :]
        cube[4, cube.shape[1] - 1, :] = np.flip(cube[4, :, cube.shape[1] - 1])
        cube[4, :, cube.shape[1] - 1] = temp


    @staticmethod
    def F(cube):
        pass



    @staticmethod
    def R(cube):
        pass

    @staticmethod
    def D(cube):
        # !!! This is actually D' !!!
        # rotating the bottom row
        temp = cube[0, -1, :].copy()
        for i in range(cube.shape[1]):
            cube[i, -1, :] = cube[i + 1, -1, :]
        cube[3, -1, :] = temp
        # rotating the upper side
        temp = cube[5, 0, :].copy()
        cube[5, 0, :] = np.flip(cube[5, :, 0])
        cube[5, :, 0] = cube[5, cube.shape[1] - 1, :]
        cube[5, cube.shape[1] - 1, :] = np.flip(cube[5, :, cube.shape[1] - 1])
        cube[5, :, cube.shape[1] - 1] = temp

    @staticmethod
    def L(cube):
        pass

    @staticmethod
    def B(cube):
        pass
