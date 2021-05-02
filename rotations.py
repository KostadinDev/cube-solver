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
