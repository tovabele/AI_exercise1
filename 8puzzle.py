import random

goal = [[1,2,3],[4,5,6],[7,8,0]]

def generate_board():
    tiles = [1,2,3,4,5,6,7,8,0]
    for i in tiles:
        while validate_board(tiles)
    for i in range(3):
        board = [[tiles[i*2+j] for j in range(3)] for i in range(3)]
    print(board)
#    return board

def validate_board(tiles):
    inversions = 0
    valid = False
    if (for i in tiles):
        if i >= (for j in tiles):
        inversions +=1
    if inversions%2 == 0:
        valid = True
    return valid

def calculate_hamming(state):
    hamming_distance = 0
    for i in range(8):
        if state[i] != goal[i]: hamming_distance += 1
    return hamming_distance

def calculate_manhattan_distance(state):
    manhattan_distance = 0

    return manhattan_distance

generate_board()
