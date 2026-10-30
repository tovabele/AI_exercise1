import heapq

import numpy as np
import board_utils as board
import node

def play_game(goal_state, start_tiles, used_heuristic):

    start_node = node.Node(start_tiles, goal_state, 0, used_heuristic)

    open_list = []
    heapq.heappush(open_list, (start_node.estimated_cost_to_goal, start_node))

    best_cost = {start_node.state: start_node.cost_from_start}

    while open_list:
        #find item with the lowest estimated cost to goal and pop of heapq
        _, current_node = heapq.heappop(open_list)

        if win(goal_state, current_node.state):
            path = reconstruct_path(current_node)

            for state in path:
                print()
                board.print_board(board.build_board(state))
            print('You win! Path length: {}'.format(len(path)))
            break

        # ignore if we already found better path for state
        if current_node.cost_from_start > best_cost[current_node.state]:
            continue

        # calculate possible successors
        # add to be explored if new or better
        #otherwise ignore
        successor_states = board.generate_successor_states(current_node)
        for state in successor_states:
            new_cost = current_node.cost_from_start + 1

            if state not in best_cost or (new_cost < best_cost[state]):
                best_cost[state] = new_cost
                successor_node = node.Node(state, goal_state, new_cost, used_heuristic, current_node)
                heapq.heappush(open_list, (successor_node.total_estimated_cost, successor_node))


def reconstruct_path(current_node):
    path = []
    while current_node is not None:
        path.append(current_node.state)
        current_node = current_node.parent
    path.reverse()
    return path
    #return path[::-1]

def win(goal_state, current_state):
    return np.array_equal(goal_state, current_state)