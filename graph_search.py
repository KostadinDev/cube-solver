import heapq
import datetime
from rotations import Rotations
from cube import Cube

# Needs to be tweaked to accommodate Cube Heuristic
class Heuristics:
    def __init__(self, heuristic_type):
        self.heuristic_type = heuristic_type

    def get_heuristic_value(self, cube):
        grid_length = pow(int(size), 2)
        if self.heuristic_type == '1':
            #Calculate Manhattan Distance
            total = 0
            for i in range(grid_length):
                if grid[i] == '':
                    #Don't count the blank tile
                    continue

                elif int(grid[i]) != i+1:
                    # Calculate change in y value
                    final_y = (int(grid[i]) - 1) // size
                    current_y = i // size
                    change_y = abs(final_y - current_y)
                    total += change_y

                    #Calculate change in x value
                    final_x = (int(grid[i]) - 1) % size
                    current_x = i % size
                    change_x = abs(final_x - current_x)
                    total += change_x
            return total
        else:
            #Calculate total misplaced blocks
            misplaced = 0
            for i in range(grid_length):
                if grid[i] == '':
                    continue
                elif int(grid[i]) != i + 1:
                    misplaced += 1
            return misplaced


# Solve the Cube (Takes in a Cube object and a Heuristic object as params)
def graph_search(cube, heuristic_obj):
    a = datetime.datetime.now()
    frontier = []
    explored = []
    #Should push (heuristic value based on current state of cube, (cube state, path)) onto frontier
    heapq.heappush(frontier, (heuristic_obj.get_heuristic_value(cube.cube), (cube.cube, '')))
    while frontier:
        temp = heapq.heappop(frontier)
        current_state, current_blank_index, path = temp[1][0], temp[1][1], temp[1][2]
        if cube.is_solved(cube):
            b = datetime.datetime.now()
            c = b - a
            print((c.total_seconds() * 1000))
            return path
        if current_state not in explored:
            explored.append(current_state)
            for move in self.get_next_possible_moves(current_state, current_blank_index, path):
                new_grid_state = move[0]
                new_blank_index = move[1]
                new_path = move[2]
                g_val = len(new_path)
                f_val = g_val + heuristic_obj.get_heuristic_value(new_grid_state, self.size)
                heapq.heappush(frontier, (f_val, (new_grid_state, new_blank_index, new_path)))
