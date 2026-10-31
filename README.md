# 8 puzzle task:

Definiton:
- State representation (tuple?)
- blank tile convention = 0
- 1 move = blank swaps with valid adjecent tile 
  (horizontally or vertically)
- goal state:
   1 2 3
   4 5 6
   7 8

## determine solvability
 - [x] check for solvability (inversions mod 2 = 0)

## calculate:
 - [x] hamming distance (count wrong elements)
 - [x] manhattan distance (add up all distance deltas)
 - [x] use A* to solve f(s) = g(s) + h(s)
    - g: costs so far
    - h: costs (hamming or manhattan) to goal

 - [x] determine next states (2-4)

 - [x] calculate Costs()

 - [x] use 'priority queues' via costs - no idea what that was

 - [x] use set for closed lists (states already fully explored)

 - [x] parent mapping: track parent nodes to reconstruct solution 
   - TBD heisst das liste aller prio nodes per state?

## simple interface
 - [x] generate puzzle
 - [ ] show time used: hamming vs manhattan
 - [ ] enter puzzle

## wunsch: show puzzle being solved
  - [x] display 3x3 grid in text mode
