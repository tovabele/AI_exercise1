import time

import board_utils
import game_utils
import heuristics

# Input: goal state, start state and the heuristic to be used
# Output: Elapsed time, expanded nodes & path for on search
# Runs one search for one start state with a set heuristic & prints the results
def run_search(goal, start_state, heuristic):

        start_time = time.perf_counter()

        search_result = game_utils.play_game(
            goal,
            start_state,
            heuristic
        )

        elapsed_time = time.perf_counter() - start_time

        return {
            "start_state": start_state,
            "elapsed_time": elapsed_time,
            "expanded_nodes": search_result['expanded_nodes'],
            "path_length": search_result['path_length'],
        }

# Input: goal, start state
# Output: Search metrics of one start state with all heuristics
# Run a search with each of the 3 heuristics (manhattan, hamming, zero)
# for the given start state
def run_all_heuristics(goal, start_state):

    return {
        "manhattan": run_search(
            goal,
            start_state,
            heuristics.calculate_manhattan_distance
        ),

        "hamming": run_search(
            goal,
            start_state,
            heuristics.calculate_hamming_distance
        ),

        "zero_heuristic": run_search(
            goal,
            start_state,
            heuristics.zero_heuristic
        )
    }

def run_experiment(goal, start_states):

    experiment_results = []

    for start_state in start_states:
        state_results = run_all_heuristics(goal, start_state)

        experiment_results.append({
            "start_state": start_state,
            "results": state_results
        })

    return experiment_results

def print_search_results(name, results):

    print(f"\n{name}")

    print(f"Running time: {results['elapsed_time']:.6f} seconds")
    print(f"Expanded nodes: {results['expanded_nodes']}")
    print(f"Path length: {results['path_length']}")

def print_experiment_results(experiment_results):

    for i, state_result in enumerate(experiment_results, start=1):
        start_state = state_result["start_state"]
        result = state_result["results"]

        print("\n" + "-" *90)
        print(f"Search {i}")
        print(f"Start state:")

        board = board_utils.build_board(start_state)
        board_utils.print_board(board)

        print_search_results("Manhattan", result["manhattan"])
        print_search_results("Hamming", result["hamming"])
        print_search_results("Zero Heuristic", result["zero_heuristic"])

