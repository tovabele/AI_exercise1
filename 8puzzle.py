import calculations
import board_utils
import run_search

#using '0' as empty field to allow inversion detection by value
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
# number of searches > 1
NUMBER_OF_SEARCHES = 100

start_states = board_utils.generate_start_states(GOAL, NUMBER_OF_SEARCHES)

experiment_results = run_search.run_experiment(GOAL, start_states)

experiment_statistics = calculations.calculate_experiment_statistics(experiment_results)

calculations.print_calculation_results(experiment_statistics)

