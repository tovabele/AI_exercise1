class Node:
    def __init__(self, state, g=0, h=0 ,parent=None):
        self.parent = parent
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h

def __lessthen__(self, other):
    return (self.f < other.f)
