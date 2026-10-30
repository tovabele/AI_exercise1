import random
import heuristics
import node

#using '0' as empty field to allow inversion detection by value
goal = (1,2,3,4,5,6,7,8,0)

def generate_starttiles(goal):
    gen_tiles = list(goal)
    random.shuffle(gen_tiles)
    while validate_board(gen_tiles) == False:
        #print(gen_tiles)
        random.shuffle(gen_tiles)
    # return a immutable object
    return tuple(gen_tiles)


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
    #test print(valid)
    if inversions%2 == 0:
        valid = True
    return valid

def build_board(b_arr):
    row_strings = []
    board = [
        [(" " if b_arr[i * 3 + j] == 0 else str(b_arr[i * 3 + j])) for j in range(3)] for i in range(3)]
    for row in board:
        row_str = " ".join(row)
        row_strings.append(row_str)
    return row_strings

# One move = blank position change
# Input = puzzle state
# Output = legal puzzle states after 1 move
# Provides the next possible states for the search
def generate_successors(current_state):
    # Find index of 0
    blank_index = 0
    for i in range(len(current_state)):
        if current_state[i] == 0:
            blank_index = i
            break

    print('0 is at', blank_index)

    #create empty list "next_states"
    next_states = []

    #find neighbor indices for blank
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

    print("Neighbor indices: ", neigh_indices)
    
    #for every neighbor index:
    for neighbor in neigh_indices:

        #make list copy of current_state
        neighbor_state = list(current_state)

        #swap blank with neighbor
        neighbor_state[blank_index], neighbor_state[neighbor] = (
            neighbor_state[neighbor],
            neighbor_state[blank_index]
        )

        #convert copy back to tuple
        #& add to next_states
        next_states.append(tuple(neighbor_state))

    #test print boards
    for state in next_states:
        board = build_board(state)
        print_board(board)
        print()

    return next_states


def print_board(board):
    for line in board:
        print (line)


# Testing
print("Goal:      ", goal)
goal_board = build_board(goal)
print_board(goal_board)

start_tiles  = generate_starttiles(goal)
print("Generated: ", start_tiles)

# new_board = start_tiles
new_board = (1,2,3,4,5,0,6,8,7)
start_board = build_board(new_board)
print()
print('Start board:')
print_board(start_board)

hamming_distance = heuristics.calculate_hamming(goal, new_board)
manhattan_dist = heuristics.calculate_manhattan_distance(goal, new_board)

print()
validity = validate_board(new_board)
print ('Validity: ', validity)
print ('Hamming distance: ', hamming_distance)
print ('Manhattan dist.:  ', manhattan_dist)

print()
generate_successors(new_board)

start_node = node.Node(start_tiles, 0, manhattan_dist)

#todos:
 # g(n) costs of path so far
 # should just g(n) +=1 with every new state explored

 # h(n) costs via heuristics man & ham
 # ...mh, tasty

# anyway. open issues:
 # follow node with lowest h(n) and sum up costs g(n) so far
 # we have preliminary h(n) colculations called
 # heuristics.calculate_hamming() and
 # heuristics.calculate_manhattan_distance()

# what even is a tuple? (without asking chaty: a two-value variable?
# e.g. (123456789, 23) would be our goal state after 23 moves

# how do we store states? he mentioned something in python, a list that returns the lowest item first...

# i wrote this down on paper which is in vienna
# how do we store previous state (so we only explore new states)?

#closed list visited states:
visitedStates = {}

#add the start node to the visited list, using its costs g
visitedStates[start_node.state] = start_node.g


# find out how many next states(without previous) we have. should be easy:
# - if tile[4] == 9  > 4(3) states
# - if tile[1 || 3 || 5 || 7] == 9 > 3(2) states
# - if tile[0 || 2 || 6 || 8] == 9 > 2(1) states
# 9 being the empty tile


