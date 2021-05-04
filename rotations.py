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
        # !!! This is R' !!!
        sides = [0, 4, 2, 5]
        temp = cube[0, :, 2].copy()

        cube[0, :, 2] = cube[4, :, 2]
        cube[4, :, 2] = cube[2, :, 0]
        cube[2, :, 0] = cube[5, :, 2]
        cube[5, :, 2] = temp.copy()

        temp = cube[1, :, 2].copy()
        cube[1, :, 0] = cube[1, cube.shape[1] - 1, :]
        cube[1, cube.shape[1] - 1, :] = np.flip(cube[1, :, 2])
        cube[1, :, 2] = cube[1, 0, :]
        cube[1, 0, :] = np.flip(temp)

    @staticmethod
    def D(cube):
        # !!! This is actually D' !!!
        # rotating the bottom row
        temp = cube[0, -1, :].copy()
        for i in range(cube.shape[1]):
            cube[i, -1, :] = cube[i + 1, -1, :]
        cube[3, -1, :] = temp
        # rotating the bottom side
        temp = cube[5, 0, :].copy()
        cube[5, 0, :] = np.flip(cube[5, :, 0])
        cube[5, :, 0] = cube[5, cube.shape[1] - 1, :]
        cube[5, cube.shape[1] - 1, :] = np.flip(cube[5, :, cube.shape[1] - 1])
        cube[5, :, cube.shape[1] - 1] = temp

    @staticmethod
    def L(cube):
        sides = [0, 4, 2, 5]
        temp = cube[0, :, 0].copy()

        cube[0, :, 0] = cube[4, :, 0]
        cube[4, :, 0] = cube[2, :, 2]
        cube[2, :, 2] = cube[5, :, 0]
        cube[5, :, 0] = temp.copy()

        temp = cube[3, :, 0].copy()
        cube[3, :, 0] = cube[3, cube.shape[1] - 1, :]
        cube[3, cube.shape[1] - 1, :] = np.flip(cube[3, :, 2])
        cube[3, :, 2] = cube[3, 0, :]
        cube[3, 0, :] = np.flip(temp)

    @staticmethod
    def B(cube):
        # !!! This is B' !!!
        sides = [1, 4, 3, 5]
        temp = cube[1, :, 2].copy()
        for i in range(len(sides) - 1):
            cube[sides[i], :, 2] = cube[sides[i + 1], :, 2]
        cube[5, :, 2] = temp.copy()

        temp = cube[2, :, 2].copy()
        cube[2, :, 0] = cube[2, cube.shape[1] - 1, :]
        cube[2, cube.shape[1] - 1, :] = np.flip(cube[2, :, 2])
        cube[2, :, 2] = cube[2, 0, :]
        cube[2, 0, :] = np.flip(temp)
