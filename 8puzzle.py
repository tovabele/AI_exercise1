import random
import heuristics

#using '9' as empty field to allow inversion detection by value
goal = [1,2,3,4,5,6,7,8,9]

state = tuple


def generate_tiles():
    #use array.copy() to prevent shuffling the original list!
    tiles =  goal.copy()
    random.shuffle(tiles)
    while validate_board(tiles) == False:
        #print(tiles)
        random.shuffle(tiles)
    return tiles

def validate_board(tiles):
    inversions = 0
    valid = False
    for i in range(len(tiles)):
        for j in range(i+1,len(tiles)):
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

tiles  = generate_tiles()
hamming_distance = heuristics.calculate_hamming(goal, tiles)
manhattan_dist = heuristics.calculate_manhattan_distance(goal, tiles)

print("Generated: ", tiles)
new_board = build_board(tiles)
print_board(new_board)
print ('Hamming distance: ', hamming_distance)
print ('Manhattan dist.   ', manhattan_dist)

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

# how do we store previous state (so we only explore new states)?

# what even is a tuple? (without asking chaty: a two-value variable?
# e.g. [123456789, 23] would be our goal state after 23 moves

# how do we store states? he mentioned something in python, a list that returns the lowest item first...
# i wrote this down on paper which is in vienna

# find out how many next states(without previous) we have. should be easy:
# - if tile[4] == 9  > 4(3) states
# - if tile[1 || 3 || 5 || 7] == 9 > 3(2) states
# - if tile[0 || 2 || 6 || 8] == 9 > 2(1) states
# 9 being the empty tile


