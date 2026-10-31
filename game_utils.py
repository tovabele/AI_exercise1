import heapq
import numpy as np
import board_utils as board
import node

def win(goal_state, current_state):
    return np.array_equal(goal_state, current_state)

def reconstruct_expanded_path(current_node, expanded_list):
    path = []
    while current_node is not None:
        if current_node.parent is None:
            path.append([current_node.state])
        else:
            path.append([current_node.state] + expanded_list[current_node.parent])
        current_node = current_node.parent
    path.reverse()
    return path
    #return path[::-1]

def print_expanded_path(current_node, expanded_dict):
    expanded_path = reconstruct_expanded_path(current_node, expanded_dict)

    for states in expanded_path:
        board.print_states(states)

    print('Path length: {}'.format(len(expanded_path)))

def play_game(goal_state, start_tiles, used_heuristic, print_output = True):

    start_node = node.Node(start_tiles, goal_state, 0, used_heuristic)

    expanded_dict = {}

    open_list = []
    heapq.heappush(open_list, (start_node.estimated_cost_to_goal, start_node))

    best_cost = {start_node.state: start_node.cost_from_start}

    while open_list:
        #find item with the lowest estimated cost to goal and pop of heapq
        _, current_node = heapq.heappop(open_list)

        if win(goal_state, current_node.state):
            if print_output:
                print_expanded_path(current_node, expanded_dict)
            break

        # ignore if we already found better path for state
        if current_node.cost_from_start > best_cost[current_node.state]:
            continue

        # calculate possible successors
        # add to be explored if new or better
        #otherwise ignore
        successor_states = board.generate_successor_states(current_node)
        expanded_dict[current_node] = successor_states
        for state in successor_states:
            new_cost = current_node.cost_from_start + 1

            if state not in best_cost or (new_cost < best_cost[state]):
                best_cost[state] = new_cost
                successor_node = node.Node(state, goal_state, new_cost, used_heuristic, current_node)
                heapq.heappush(open_list, (successor_node.total_estimated_cost, successor_node))

    return len(expanded_dict), len(open_list)