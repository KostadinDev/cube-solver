from cube import Cube


class DataLoader(object):
    def __init__(self, num_cubes, num_batches):
        self.cubes = [[Cube.solved_cube() for i in range(num_batches)] for j in range(num_cubes)]
        self.num_cubes = num_cubes
        self.num_batches = num_batches

    def scramble(self, num_cubes, num_batches):
        for i in range(num_cubes):
            for j in range(1, num_batches):
                self.cubes[i][j].cube = self.cubes[i][j - 1].cube.copy()
                self.cubes[i][j].random_rotate()

