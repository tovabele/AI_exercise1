import random
from random import shuffle

goal = [1,2,3,4,5,6,7,8,9]

def generate_tiles():
    tiles = [1,2,3,4,5,6,7,8,9]
    random.shuffle(tiles)
#    for i in tiles:
    while validate_board(tiles) == False:
        random.shuffle(tiles)
    #test print(tiles)
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
    for i in range(len(state)):
        if state[i] != goal[i]: hamming_distance += 1
    return hamming_distance

def calculate_manhattan_distance(state):
    manhattan_distance = 0
    for i in range(len(goal)):
        disty = 0
        for row in range(3):
            distx = 0
            disty += 1
            manhattan_distance += 1
            for col in range(3):
                distx +=1
                if state[col * 3 + row] == goal[i]:
                    manhattan_distance += disty + distx
    return manhattan_distance

def build_board(tiles):
    row_strings = []
    board = [
        [(" " if tiles[i * 3 + j] == 9 else str(tiles[i * 3 + j])) for j in range(3)] for i in range(3)]
    for row in board:
        row_str = " ".join(row)
        row_strings.append(row_str)
    return row_strings

def print_board(board):
    for line in board:
        print (line)

tiles  = generate_tiles()
hamming_distance = calculate_hamming(tiles)
manhattan_dist = calculate_manhattan_distance(tiles)

print("Goal:      ", goal)
goal_board = build_board(goal)
print_board(goal_board)

print("Generated: ", tiles)
new_board = build_board(tiles)
print_board(new_board)
print ('Hamming distance: ', hamming_distance)
print ('Manhattan dist.   ', manhattan_dist)

