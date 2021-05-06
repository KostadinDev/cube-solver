import numpy as np
from pyTwistyScrambler import scrambler333, scrambler222, scrambler444, \
    megaminxScrambler, squareOneScrambler, ftoScrambler, rexScrambler
import random
from rotations import Rotations


class Cube:
    '''
    cube[side][row][col]

    0: green
    1: red
    2: blue
    3: orange
    4: white
    5: yellow
    '''

    def __init__(self, cube=None, movelist=[]):
        # 3d numpy array: cube[side][row][col]
        self.cube = cube if cube is not None else Cube.solved_cube()
        # documents the moves made to reach this state
        self.movelist = movelist
        self.shape = self.cube.shape

    def __str__(self):
        return str(self.cube)

    # returns a randomly shuffled cube
    @staticmethod
    def random_cube():
        shuffle_sequence = scrambler222.get_WCA_scramble().split(' ')
        solved_cube = Cube.solved_cube()
        for move in shuffle_sequence:
            solved_cube.rotate(move)
        return solved_cube

    # returns a solved cube
    @staticmethod
    def solved_cube():
        configuration = np.zeros((6, 2, 2), dtype='uint8')
        for side in range(6):
            configuration[side] = np.ones((2, 2), dtype='uint8') * side
        return Cube(configuration)

    # returns the possible actions of a cube
    def actions(self):
        return ['F', 'R', 'D', 'U', 'L', 'B',
                'F\'', 'R\'', 'D\'', 'U\'', 'L\'', 'B\'',
                'F2', 'R2', 'D2', 'U2', 'L2', 'B2']

    def random_action(self):
        return random.choice(self.actions())

    def random_rotate(self):
        self.rotate(self.random_action())

    # rotates a side of the cube according to standard notation
    def rotate(self, move):
        self.movelist.append(move)
        if move == "U":
            Rotations.U(self.cube)
        elif move == "U2":
            for i in range(2):
                Rotations.U(self.cube)
        elif move == "U'":
            for i in range(3):
                Rotations.U(self.cube)
        elif move == "D'":
            Rotations.D(self.cube)
        elif move == "D2":
            for i in range(2):
                Rotations.D(self.cube)
        elif move == "D":
            for i in range(3):
                Rotations.D(self.cube)
        elif move == "L":
            Rotations.L(self.cube)
        elif move == "L2":
            for i in range(2):
                Rotations.L(self.cube)
        elif move == "L'":
            for i in range(3):
                Rotations.L(self.cube)
        elif move == "R'":
            Rotations.R(self.cube)
        elif move == "R2":
            for i in range(2):
                Rotations.R(self.cube)
        elif move == "R":
            for i in range(3):
                Rotations.R(self.cube)
        elif move == "F":
            Rotations.F(self.cube)
        elif move == "F2":
            for i in range(2):
                Rotations.F(self.cube)
        elif move == "F'":
            for i in range(3):
                Rotations.F(self.cube)
        elif move == "B":
            Rotations.B(self.cube)
        elif move == "B2":
            for i in range(2):
                Rotations.B(self.cube)
        elif move == "B'":
            for i in range(3):
                Rotations.B(self.cube)

    # checks if solved
    def is_solved(self):
        for i in range(self.cube.shape[0]):
            if self.cube[i, :, :].sum() != i * self.cube.shape[1] * self.cube.shape[2]:
                return False
        return True
