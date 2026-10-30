import heuristics
import board_utils
from board_utils import build_board, print_board, generate_start_tiles, validate_board, generate_successor_states
import run_search

#using '0' as empty field to allow inversion detection by value
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
NUMBER_OF_SEARCHES = 10

start_states = run_search.generate_start_states(GOAL, NUMBER_OF_SEARCHES)
for i, start_state in enumerate(start_states, start=1):
    board = build_board(start_state)
    print('-------------------------------------------------------------------------------------------------------')
    print(f'Search {i}')
    print_board(board)
    print(f'\nMANHATTAN: ')
    manhattan = run_search.run_search(GOAL, start_state, heuristics.calculate_manhattan_distance)
    print(f'\nHAMMING: ')
    hamming = run_search.run_search(GOAL, start_state, heuristics.calculate_hamming_distance)
    print(f'\nZERO ')
    zero = run_search.run_search(GOAL, start_state, heuristics.zero_heuristic)


# start_tiles  = generate_start_tiles(GOAL)

# new_board = start_tiles
# new_board = (4, 7, 5, 8, 3, 2, 1, 6, 0)
# start_board = build_board(new_board)
# print_board(start_board)

# if not validate_board(new_board):
#     exit()

# game = game_utils.play_game(GOAL, new_board, heuristics.calculate_manhattan_distance)
# game_utils.play_game(GOAL, new_board, heuristics.calculate_hamming_distance)
# game_utils.play_game(GOAL, new_board, heuristics.zero_heuristic)


# todos:
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


