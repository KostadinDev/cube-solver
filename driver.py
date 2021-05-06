from cube import Cube

if __name__ == '__main__':
    allowed_rotations = ['F', 'R', 'D', 'U', 'L', 'B',
                         'F\'', 'R\'', 'D\'', 'U\'', 'L\'', 'B\'',
                         'F2', 'R2', 'D2', 'U2', 'L2', 'B2']

    cube = Cube.random_cube()
    print(cube)