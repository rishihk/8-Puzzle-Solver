# Citations: Aimacode, GitHub. https://github.com/aimacode 

import sys
from collections import deque
from queue import PriorityQueue
import argparse
import time
import itertools
import heapq
import math
import os

class Node: # Class for the nodes in the search tree
    
    def __init__(self, state, parent=None, action=None, path_cost=0): # Constructor
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self): 
        return "<Node {}>".format(self.state) # String representation of the node

    def __lt__(self, node): 
        return self.state < node.state # Compare nodes based on their states

    def expand(self, problem):
        return [self.child_node(problem, action) for action in problem.actions(self.state)] # Expand the node to get its children

    def child_node(self, problem, action): 
        next_state = problem.result(self.state, action) # Get the next state from the result of the action
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state)) # Create a new node for the next state
        return next_node # Return the new node

    def solution(self):
        return [node.action for node in self.path()[1:]] # Get the solution path

    def path(self):
        node, path_back = self, [] # Get the path from the current node to the root node
        while node:
            path_back.append(node) # Append the current node to the path
            node = node.parent     # Move to the parent node
        return list(reversed(path_back)) # Return the reversed path

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state # Compare nodes based on their states

    def __hash__(self):
        return hash(self.state) # Hash the state of the node
