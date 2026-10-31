import heuristics
from board_utils import validate_board

class Node:
    def __init__(self, state, goal_state, cost_from_start=0, heuristic=heuristics.calculate_hamming_distance, parent=None):
        self.parent = parent
        self.state = state
        self.heuristic = heuristic
        self.cost_from_start = cost_from_start
        self.estimated_cost_to_goal = self._calculate_estimated_cost(goal_state)
        self.total_estimated_cost = self.cost_from_start + self.estimated_cost_to_goal

    def __lt__(self, other):
        return self.total_estimated_cost < other.total_estimated_cost

    def validate_board_state(self):
        return validate_board(self.state)

    def _calculate_estimated_cost(self, goal_state):
        return self.heuristic(goal_state, self.state)