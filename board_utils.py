import numpy as np

def build_board(board_array):
    return np.reshape(board_array, (-1, 3))

def print_board(board):
    print(np.matrix(board))

def print_states(states):
    boards = []
    for state in states:
        boards.append(build_board(state))

    for rows in zip(*boards):
        first_board = " ".join(str(tile) for tile in rows[0])
        other_boards = "    ".join(
            " ".join(str(tile) for tile in row)
            for row in rows[1:]
        )

        if other_boards:
            print(first_board + "  |  " + other_boards)
        else:
            print(first_board)
    print()

def validate_board(tiles):
    inversions = 0

    valid = False
    for i in range(len(tiles)):
        for j in range(i+1,len(tiles)):
            #ignore blank tile
            if tiles[i] == 0 or tiles[j] == 0:
                continue
            if tiles[i] > tiles[j]:
                inversions +=1

    if inversions%2 == 0:
        valid = True
    return valid

def generate_start_tiles(goal):
    gen_tiles = list(goal)
    np.random.shuffle(gen_tiles)
    while not validate_board(gen_tiles):
        np.random.shuffle(gen_tiles)
    # return immutable object
    return tuple(gen_tiles)

# One move = blank position change
# Input = puzzle state
# Output = legal puzzle states after 1 move
# Provides the next possible states for the search
def generate_successor_states(node):
    # Find index of 0
    blank_index = 0
    for i in range(len(node.state)):
        if node.state[i] == 0:
            blank_index = i
            break

    # print('0 is at', blank_index)
    # create empty list "next_states"
    next_states = []

    # find neighbor indices for blank
    neigh_indices = []

    row = blank_index // 3
    col = blank_index % 3

    if row > 0:
        neighbor = blank_index - 3
        neigh_indices.append(neighbor)
    if row < 2:
        neighbor = blank_index + 3
        neigh_indices.append(neighbor)
    if col > 0:
        neighbor = blank_index - 1
        neigh_indices.append(neighbor)
    if col < 2:
        neighbor = blank_index + 1
        neigh_indices.append(neighbor)

    # for every neighbor index:
    for neighbor in neigh_indices:
        # make list copy of current_state
        neighbor_state = list(node.state)

        # swap blank with neighbor
        neighbor_state[blank_index], neighbor_state[neighbor] = (
            neighbor_state[neighbor],
            neighbor_state[blank_index]
        )

        # convert copy back to tuple and add to next_states
        next_states.append(tuple(neighbor_state))

    return next_states