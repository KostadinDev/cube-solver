import heapq
import datetime
from rotations import Rotations
from cube import Cube
import numpy as np
import random
import copy

# Solve the Cube (Takes in a Cube object and a Heuristic object as params)
def graph_search(cube):
    a = datetime.datetime.now()
    frontier = []
    explored = []
    #Should push (heuristic value based on current state of cube, (cube state, path)) onto frontier
    heapq.heappush(frontier, (get_heuristic_value(cube), (cube.cube, cube, [])))
    while frontier:
        temp = heapq.heappop(frontier)
        current_state, cube_obj, path = temp[1][0], temp[1][1], temp[1][2]
        if cube_obj.is_solved():
            b = datetime.datetime.now()
            c = b - a
            print((c.total_seconds() * 1000))
            return current_state, path
        if str(current_state) not in explored:
            explored.append(str(current_state))
            for move in get_next_possible_moves(cube_obj, path):
                print(frontier)
                new_grid_state = move[0]
                new_cube_obj = move[1]
                new_path = move[2]
                g_val = len(new_path)
                f_val = g_val + get_heuristic_value(new_cube_obj)
                # print(f_val)
                heapq.heappush(frontier, (f_val, (new_grid_state, new_path)))

#Advanced move pruning: Let three of the faces be "first" faces,
# and three of them be "second" faces, where the second faces are
# opposite the first faces. Here the rule is that after you move a first face,
# you can move any of the other faces - so there will be 15 moves.
# But, after you move a second face,
# you can't move the same face again or the opposite first face.
# In this case the branching factor is 12. The overall branching factor is then around 13.
def get_next_possible_moves(cube_obj, path):
    pick_a_move = ['R', 'F', 'T', 'L', 'B', 'D']
    last_move = ''
    if path:
        last_move = path[-1]
        #Remove last_move from pick_a_move_array
        pick_a_move.remove(last_move)
    returned = []
    # L, B, and D are "second" faces
    if last_move == 'L':
        pick_a_move.remove('R')
    elif last_move == 'B':
        pick_a_move.remove('F')
    elif last_move == 'D':
        pick_a_move.remove('T')

    for move in pick_a_move:
        new_cube = copy.deepcopy(cube_obj)
        new_cube.rotate(move)
        new_path = []
        if path:
            new_path = path.copy()
        new_path.append(move)
        returned.append((new_cube.cube, new_cube, new_path))
    return returned


def get_heuristic_value(cube):
    cube = cube.cube
    # Calculate total misplaced cubies
    # Finds the number of unique cubie values for each face and totals them. The higher the value, the further from the goal
    unique_cubies_total = 0
    for i in range(len(cube)):
        unique = set()
        for j in range(len(cube[i])):
            for k in range(len(cube[i][j])):
                # print("Cubie: " + str(cube[i][j][k]))
                unique.add(cube[i][j][k])
        # print("Uniques for side " + str(i) + ": " + str(len(unique)))
        unique_cubies_total += len(unique)
    return unique_cubies_total


print("Start:")
random_cube = Cube.random_cube()
returned_cube, path = graph_search(random_cube)
print("Solved!")
print(returned_cube)
print("Path:")
print(path)