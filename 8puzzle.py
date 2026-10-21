import random
from random import shuffle

def generate_tiles():
    tiles =  [1,2,3,4,5,6,7,8,9]
    random.shuffle(tiles)
    while validate_board(tiles) == False:
        #print(tiles)
        random.shuffle(tiles)
    return tiles

def validate_board(tiles):
    inversions = 0
    valid = False
    for i in range(len(tiles)):
        for j in range(i+1,len(tiles)):
            if tiles[i] >= tiles[j]:
                inversions +=1
    #test print(valid)
    if inversions%2 == 0:
        valid = True
    return valid

def calculate_hamming(state):
    hamming_distance = 0
    for i in range(len(state)-1):
        if state[i] != goal[i]: hamming_distance += 1
    return hamming_distance

def calculate_manhattan_distance(state):
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

def build_board(b_arr):
    row_strings = []
    board = [
        [(" " if b_arr[i * 3 + j] == 9 else str(b_arr[i * 3 + j])) for j in range(3)] for i in range(3)]
    for row in board:
        row_str = " ".join(row)
        row_strings.append(row_str)
    return row_strings

def print_board(board):
    for line in board:
        print (line)

goal = [1,2,3,4,5,6,7,8,9]
print("Goal:      ", goal)
goal_board = build_board(goal)
print_board(goal_board)

tiles  = generate_tiles()
hamming_distance = calculate_hamming(tiles)
manhattan_dist = calculate_manhattan_distance(tiles)

print("Generated: ", tiles)
new_board = build_board(tiles)
print_board(new_board)
print ('Hamming distance: ', hamming_distance)
print ('Manhattan dist.   ', manhattan_dist)

