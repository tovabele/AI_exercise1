import random
import heuristics
import node

#using '0' as empty field
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
            if tiles[i] != 0:
                continue
            if tiles[i] >= tiles[j]:
                inversions +=1
    #test print(valid)
    if inversions%2 == 0:
        valid = True
    return valid


def build_board(b_arr):
    row_strings = []
    board = [
        [(" " if b_arr[i * 3 + j] == 9 else str(b_arr[i * 3 + j])) for j in range(3)] for i in range(3)]
    for row in board:
        row_str = " ".join(row)
        row_strings.append(row_str)
    return row_strings

def print_board(board):
    for line in board:
        print (line)

print("Goal:      ", goal)
goal_board = build_board(goal)
print_board(goal_board)

start_tiles  = generate_starttiles(goal)

hamming_distance = heuristics.calculate_hamming(goal, start_tiles)
manhattan_dist = heuristics.calculate_manhattan_distance(goal, start_tiles)

# print("Generated: ", start_tiles)
# new_board = build_board(start_tiles)
# print_board(new_board)
new_board = (1,0,2,3,4,5,6,7,8)
validity = validate_board(new_board)
print ('Solvable: ' , validity)
print ('Hamming distance: ', hamming_distance)
print ('Manhattan dist.   ', manhattan_dist)

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


