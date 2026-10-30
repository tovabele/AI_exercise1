import time

import board_utils
import game_utils
import heuristics

def generate_start_states(goal, number_of_states):
    start_states = []

    while len(start_states) < number_of_states:
        start_state = board_utils.generate_start_tiles(goal)
        if board_utils.validate_board(start_state):
            start_states.append(start_state)

    return start_states

def run_search(goal, start_state, heuristic):
        start_time = time.perf_counter()

        search = game_utils.play_game(
            goal,
            start_state,
            heuristic
        )

        elapsed_time = time.perf_counter() - start_time

        print('Running time:', elapsed_time, 'seconds')
        print('Expanded nodes:' , search['expanded_nodes'])
        return [elapsed_time, search['expanded_nodes']]



