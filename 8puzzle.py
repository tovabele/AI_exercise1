import heuristics
import board_utils
from board_utils import build_board, print_board, generate_start_tiles, validate_board, generate_successor_states
import run_search

#using '0' as empty field to allow inversion detection by value
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
NUMBER_OF_SEARCHES = 10

start_states = board_utils.generate_start_states(GOAL, NUMBER_OF_SEARCHES)

experiment_results = run_search.run_experiment(GOAL, start_states)

run_search.print_experiment_results(experiment_results)

