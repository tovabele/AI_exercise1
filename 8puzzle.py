import random
from random import shuffle

goal = [[1,2,3],[4,5,6],[7,8,9]]

def generate_board():
    tiles = [1,2,3,4,5,6,7,8,9]
    random.shuffle(tiles)
#    for i in tiles:
    while validate_board(tiles) == False:
        random.shuffle(tiles)

    board = [[tiles[i * 3 + j] for j in range(3)] for i in range(3)]

    print(tiles)
    print("Goal:      ",goal)
    print("Generated: ",board)
#    return board

def validate_board(tiles):
    inversions = 0
    valid = False
    for i in range(len(tiles)):
        for j in range(i+1,len(tiles)):
            if tiles[i] >= tiles[j]:
                inversions +=1
    print(valid)
    if inversions%2 == 0:
        valid = True
    return valid

def calculate_hamming(state):
    hamming_distance = 0
    for i in state:
        for j in goal:
            if i != j: hamming_distance += 1
    return hamming_distance

def calculate_manhattan_distance(state):
    manhattan_distance = 0

    return manhattan_distance

generate_board()
