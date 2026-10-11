8 puzzle task:

generate rnd board
 - or use fisher-yates: swap from n-1 bis 1 

determin solvability
 - check for solvability (inversions mod 2 = 0)

calculate:
 - hamming distance (count wrong elements)
 - manhattan distance (add up all distance deltas)
 - use A* to solve f(s) = g(s) + h(s) 
    g: costs so far
    h: costs (hamming or manhattan) to goal

determine next states (2-4)

calculate Costs()

use 'priority queues' via costs
 - no idea what that was

use set for closed lists (states already fully explored)

parent mapping: track parent nodes to reconstruct solution 
 - TBD heisst das liste aller prio nodes per state?

simple interface 
 - enter puzzle
 - generate puzzle
 - show time used: hamming vs manhattan

+ wunsch: show puzzle being solved
    - display 3x3 grid in text mode


