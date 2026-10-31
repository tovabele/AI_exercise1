import heuristics
from board_utils import build_board, generate_start_tiles, validate_board, generate_successor_states
import game_utils

#using '0' as empty field to allow inversion detection by value
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

start_tiles  = generate_start_tiles(GOAL)

new_board = start_tiles
#new_board = (4, 7, 5, 8, 3, 2, 1, 6, 0)
start_board = build_board(new_board)

if not validate_board(new_board):
    exit()

#game_utils.play_game(GOAL, new_board, heuristics.calculate_manhattan_distance)
#game_utils.play_game(GOAL, new_board, heuristics.calculate_hamming_distance)
(seen_states, states_in_queue) = game_utils.play_game(GOAL, new_board, heuristics.zero_heuristic)

print("Calculated states: {}".format(seen_states))
print("Queued states: {}".format(states_in_queue))
#todos:
# open issues:
# check:
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
#visitedStates[start_node.state] = start_node.cost_from_start


# find out how many next states(without previous) we have. should be easy:
# - if tile[4] == 9  > 4(3) states
# - if tile[1 || 3 || 5 || 7] == 9 > 3(2) states
# - if tile[0 || 2 || 6 || 8] == 9 > 2(1) states
# 9 being the empty tile


