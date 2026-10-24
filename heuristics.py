def calculate_hamming(goal, state):
    hamming_distance = 0
    for i in range(len(state)-1):
        if state[i] != goal[i]: hamming_distance += 1
    return hamming_distance

def calculate_manhattan_distance(goal, state):
    manhattan_distance = 0
    for i in range(8):
        print(manhattan_distance)
        for row_state in range(3):
            for col_state in range(3):
                row_goal = int(i/3)
                col_goal = i%(3)
                if state[row_state * 3 + col_state] == goal[i]:
                    manhattan_distance += abs(row_state - row_goal)
                    manhattan_distance += abs(col_state - col_goal)

    return manhattan_distance
